
# Results vs. base

- fork: faster-cpython
- ref: optimizer_api
- machine: linux-x86_64
- commit hash: c991ccb
- commit date: 2023-05-24
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230519-linux-x86_64-python-c26d03d5d6da94367c7f-3.12.0a7+-c26d03d | bm-20230524-linux-x86_64-faster%2dcpython-optimizer_api-3.12.0a7+-c991ccb |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 269 ms                                                                 | 271 ms: 1.01x slower                                                      |
| tornado_http   | 102 ms                                                                 | 99.4 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230519-linux-x86_64-python-c26d03d5d6da94367c7f-3.12.0a7+-c26d03d | bm-20230524-linux-x86_64-faster%2dcpython-optimizer_api-3.12.0a7+-c991ccb |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 196 ms                                                                 | 197 ms: 1.00x slower                                                      |
| float          | 80.8 ms                                                                | 82.0 ms: 1.02x slower                                                     |
| nbody          | 89.5 ms                                                                | 91.4 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230519-linux-x86_64-python-c26d03d5d6da94367c7f-3.12.0a7+-c26d03d | bm-20230524-linux-x86_64-faster%2dcpython-optimizer_api-3.12.0a7+-c991ccb |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 22.7 ms                                                                | 22.4 ms: 1.01x faster                                                     |
| regex_compile  | 144 ms                                                                 | 145 ms: 1.01x slower                                                      |
| regex_effbot   | 3.77 ms                                                                | 3.83 ms: 1.02x slower                                                     |
| regex_dna      | 204 ms                                                                 | 210 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230519-linux-x86_64-python-c26d03d5d6da94367c7f-3.12.0a7+-c26d03d | bm-20230524-linux-x86_64-faster%2dcpython-optimizer_api-3.12.0a7+-c991ccb |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_loads           | 24.9 us                                                                | 24.7 us: 1.01x faster                                                     |
| json_dumps           | 9.87 ms                                                                | 9.82 ms: 1.00x faster                                                     |
| xml_etree_generate   | 85.5 ms                                                                | 85.7 ms: 1.00x slower                                                     |
| unpickle_pure_python | 217 us                                                                 | 217 us: 1.00x slower                                                      |
| tomli_loads          | 2.19 sec                                                               | 2.21 sec: 1.01x slower                                                    |
| pickle               | 10.7 us                                                                | 10.8 us: 1.01x slower                                                     |
| pickle_list          | 4.56 us                                                                | 4.63 us: 1.02x slower                                                     |
| unpickle             | 14.5 us                                                                | 14.8 us: 1.02x slower                                                     |
| unpickle_list        | 4.90 us                                                                | 5.09 us: 1.04x slower                                                     |
| pickle_dict          | 30.9 us                                                                | 32.6 us: 1.05x slower                                                     |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (4): xml_etree_parse, pickle_pure_python, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230519-linux-x86_64-python-c26d03d5d6da94367c7f-3.12.0a7+-c26d03d | bm-20230524-linux-x86_64-faster%2dcpython-optimizer_api-3.12.0a7+-c991ccb |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 9.33 ms                                                                | 9.34 ms: 1.00x slower                                                     |
| python_startup_no_site | 6.78 ms                                                                | 6.79 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230519-linux-x86_64-python-c26d03d5d6da94367c7f-3.12.0a7+-c26d03d | bm-20230524-linux-x86_64-faster%2dcpython-optimizer_api-3.12.0a7+-c991ccb |
|-----------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 10.6 ms                                                                | 10.9 ms: 1.03x slower                                                     |

All benchmarks:
===============

| Benchmark               | bm-20230519-linux-x86_64-python-c26d03d5d6da94367c7f-3.12.0a7+-c26d03d | bm-20230524-linux-x86_64-faster%2dcpython-optimizer_api-3.12.0a7+-c991ccb |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| gc_traversal            | 3.94 ms                                                                | 3.82 ms: 1.03x faster                                                     |
| pyflate                 | 456 ms                                                                 | 444 ms: 1.03x faster                                                      |
| spectral_norm           | 108 ms                                                                 | 106 ms: 1.03x faster                                                      |
| tornado_http            | 102 ms                                                                 | 99.4 ms: 1.03x faster                                                     |
| telco                   | 6.95 ms                                                                | 6.83 ms: 1.02x faster                                                     |
| deepcopy_reduce         | 3.19 us                                                                | 3.14 us: 1.02x faster                                                     |
| pathlib                 | 18.7 ms                                                                | 18.5 ms: 1.01x faster                                                     |
| crypto_pyaes            | 79.2 ms                                                                | 78.1 ms: 1.01x faster                                                     |
| logging_silent          | 101 ns                                                                 | 99.8 ns: 1.01x faster                                                     |
| regex_v8                | 22.7 ms                                                                | 22.4 ms: 1.01x faster                                                     |
| logging_simple          | 6.40 us                                                                | 6.33 us: 1.01x faster                                                     |
| async_tree_none         | 469 ms                                                                 | 466 ms: 1.01x faster                                                      |
| json_loads              | 24.9 us                                                                | 24.7 us: 1.01x faster                                                     |
| pycparser               | 1.21 sec                                                               | 1.20 sec: 1.01x faster                                                    |
| logging_format          | 7.06 us                                                                | 7.01 us: 1.01x faster                                                     |
| deltablue               | 3.51 ms                                                                | 3.49 ms: 1.01x faster                                                     |
| asyncio_tcp             | 516 ms                                                                 | 513 ms: 1.01x faster                                                      |
| json_dumps              | 9.87 ms                                                                | 9.82 ms: 1.00x faster                                                     |
| create_gc_cycles        | 1.51 ms                                                                | 1.50 ms: 1.00x faster                                                     |
| scimark_monte_carlo     | 72.6 ms                                                                | 72.3 ms: 1.00x faster                                                     |
| raytrace                | 299 ms                                                                 | 298 ms: 1.00x faster                                                      |
| asyncio_tcp_ssl         | 1.80 sec                                                               | 1.79 sec: 1.00x faster                                                    |
| python_startup          | 9.33 ms                                                                | 9.34 ms: 1.00x slower                                                     |
| python_startup_no_site  | 6.78 ms                                                                | 6.79 ms: 1.00x slower                                                     |
| hexiom                  | 6.16 ms                                                                | 6.17 ms: 1.00x slower                                                     |
| xml_etree_generate      | 85.5 ms                                                                | 85.7 ms: 1.00x slower                                                     |
| unpickle_pure_python    | 217 us                                                                 | 217 us: 1.00x slower                                                      |
| pidigits                | 196 ms                                                                 | 197 ms: 1.00x slower                                                      |
| sqlglot_parse           | 1.33 ms                                                                | 1.34 ms: 1.00x slower                                                     |
| pprint_pformat          | 1.50 sec                                                               | 1.51 sec: 1.01x slower                                                    |
| regex_compile           | 144 ms                                                                 | 145 ms: 1.01x slower                                                      |
| fannkuch                | 385 ms                                                                 | 388 ms: 1.01x slower                                                      |
| scimark_sor             | 124 ms                                                                 | 125 ms: 1.01x slower                                                      |
| coverage                | 95.9 ms                                                                | 96.7 ms: 1.01x slower                                                     |
| pprint_safe_repr        | 735 ms                                                                 | 741 ms: 1.01x slower                                                      |
| 2to3                    | 269 ms                                                                 | 271 ms: 1.01x slower                                                      |
| tomli_loads             | 2.19 sec                                                               | 2.21 sec: 1.01x slower                                                    |
| richards                | 44.4 ms                                                                | 44.8 ms: 1.01x slower                                                     |
| coroutines              | 22.4 ms                                                                | 22.6 ms: 1.01x slower                                                     |
| pickle                  | 10.7 us                                                                | 10.8 us: 1.01x slower                                                     |
| sqlalchemy_declarative  | 145 ms                                                                 | 147 ms: 1.01x slower                                                      |
| meteor_contest          | 105 ms                                                                 | 106 ms: 1.01x slower                                                      |
| float                   | 80.8 ms                                                                | 82.0 ms: 1.02x slower                                                     |
| pickle_list             | 4.56 us                                                                | 4.63 us: 1.02x slower                                                     |
| regex_effbot            | 3.77 ms                                                                | 3.83 ms: 1.02x slower                                                     |
| go                      | 135 ms                                                                 | 138 ms: 1.02x slower                                                      |
| comprehensions          | 20.6 us                                                                | 20.9 us: 1.02x slower                                                     |
| deepcopy_memo           | 37.7 us                                                                | 38.4 us: 1.02x slower                                                     |
| unpickle                | 14.5 us                                                                | 14.8 us: 1.02x slower                                                     |
| generators              | 31.4 ms                                                                | 32.1 ms: 1.02x slower                                                     |
| nbody                   | 89.5 ms                                                                | 91.4 ms: 1.02x slower                                                     |
| nqueens                 | 80.8 ms                                                                | 82.6 ms: 1.02x slower                                                     |
| scimark_fft             | 347 ms                                                                 | 356 ms: 1.02x slower                                                      |
| regex_dna               | 204 ms                                                                 | 210 ms: 1.03x slower                                                      |
| mako                    | 10.6 ms                                                                | 10.9 ms: 1.03x slower                                                     |
| unpickle_list           | 4.90 us                                                                | 5.09 us: 1.04x slower                                                     |
| scimark_sparse_mat_mult | 4.75 ms                                                                | 4.94 ms: 1.04x slower                                                     |
| pickle_dict             | 30.9 us                                                                | 32.6 us: 1.05x slower                                                     |
| unpack_sequence         | 45.8 ns                                                                | 59.7 ns: 1.30x slower                                                     |
| Geometric mean          | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (26): async_tree_memoization, sqlalchemy_imperative, xml_etree_parse, async_tree_cpu_io_mixed, mdp, chaos, typing_runtime_protocols, pickle_pure_python, json, bench_thread_pool, sqlglot_optimize, dask, mypy2, sqlglot_transpile, bench_mp_pool, docutils, deepcopy, richards_super, async_tree_io, sqlglot_normalize, dulwich_log, xml_etree_process, xml_etree_iterparse, sqlite_synth, scimark_lu, async_generators
