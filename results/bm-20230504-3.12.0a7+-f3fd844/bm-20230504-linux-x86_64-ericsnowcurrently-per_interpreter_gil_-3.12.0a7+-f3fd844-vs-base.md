
# Results vs. base

- fork: ericsnowcurrently
- ref: per_interpreter_gil_
- machine: linux-x86_64
- commit hash: f3fd844
- commit date: 2023-05-04
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230503-linux-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 271 ms                                                                 | 272 ms: 1.00x slower                                                              |
| tornado_http   | 99.5 ms                                                                | 100 ms: 1.01x slower                                                              |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                      |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230503-linux-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 83.2 ms                                                                | 82.4 ms: 1.01x faster                                                             |
| pidigits       | 197 ms                                                                 | 197 ms: 1.00x slower                                                              |
| nbody          | 87.5 ms                                                                | 90.1 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230503-linux-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 3.69 ms                                                                | 3.66 ms: 1.01x faster                                                             |
| regex_v8       | 22.1 ms                                                                | 22.2 ms: 1.00x slower                                                             |
| regex_compile  | 145 ms                                                                 | 146 ms: 1.00x slower                                                              |
| regex_dna      | 200 ms                                                                 | 204 ms: 1.02x slower                                                              |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230503-linux-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_list        | 5.02 us                                                                | 4.83 us: 1.04x faster                                                             |
| unpickle             | 15.0 us                                                                | 14.6 us: 1.03x faster                                                             |
| json_loads           | 25.8 us                                                                | 25.1 us: 1.03x faster                                                             |
| pickle_dict          | 30.7 us                                                                | 30.4 us: 1.01x faster                                                             |
| xml_etree_generate   | 84.7 ms                                                                | 85.1 ms: 1.01x slower                                                             |
| xml_etree_process    | 59.2 ms                                                                | 59.9 ms: 1.01x slower                                                             |
| unpickle_pure_python | 219 us                                                                 | 222 us: 1.01x slower                                                              |
| pickle_list          | 4.50 us                                                                | 4.57 us: 1.02x slower                                                             |
| json_dumps           | 9.98 ms                                                                | 10.1 ms: 1.02x slower                                                             |
| pickle               | 10.5 us                                                                | 10.7 us: 1.02x slower                                                             |
| pickle_pure_python   | 313 us                                                                 | 320 us: 1.02x slower                                                              |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                      |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230503-linux-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 6.73 ms                                                                | 6.69 ms: 1.01x faster                                                             |
| python_startup         | 9.20 ms                                                                | 9.14 ms: 1.01x faster                                                             |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230503-linux-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-----------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako      | 10.7 ms                                                                | 10.6 ms: 1.00x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20230503-linux-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mdp                     | 2.75 sec                                                               | 2.61 sec: 1.05x faster                                                            |
| scimark_sparse_mat_mult | 5.01 ms                                                                | 4.75 ms: 1.05x faster                                                             |
| unpack_sequence         | 51.1 ns                                                                | 49.1 ns: 1.04x faster                                                             |
| unpickle_list           | 5.02 us                                                                | 4.83 us: 1.04x faster                                                             |
| json                    | 5.01 ms                                                                | 4.82 ms: 1.04x faster                                                             |
| scimark_fft             | 367 ms                                                                 | 355 ms: 1.03x faster                                                              |
| unpickle                | 15.0 us                                                                | 14.6 us: 1.03x faster                                                             |
| json_loads              | 25.8 us                                                                | 25.1 us: 1.03x faster                                                             |
| coroutines              | 23.7 ms                                                                | 23.1 ms: 1.02x faster                                                             |
| richards                | 45.0 ms                                                                | 44.1 ms: 1.02x faster                                                             |
| create_gc_cycles        | 1.49 ms                                                                | 1.46 ms: 1.02x faster                                                             |
| sqlite_synth            | 2.72 us                                                                | 2.69 us: 1.01x faster                                                             |
| sqlglot_parse           | 1.35 ms                                                                | 1.34 ms: 1.01x faster                                                             |
| pyflate                 | 451 ms                                                                 | 446 ms: 1.01x faster                                                              |
| float                   | 83.2 ms                                                                | 82.4 ms: 1.01x faster                                                             |
| regex_effbot            | 3.69 ms                                                                | 3.66 ms: 1.01x faster                                                             |
| scimark_monte_carlo     | 73.6 ms                                                                | 73.0 ms: 1.01x faster                                                             |
| pickle_dict             | 30.7 us                                                                | 30.4 us: 1.01x faster                                                             |
| python_startup_no_site  | 6.73 ms                                                                | 6.69 ms: 1.01x faster                                                             |
| python_startup          | 9.20 ms                                                                | 9.14 ms: 1.01x faster                                                             |
| comprehensions          | 23.3 us                                                                | 23.2 us: 1.01x faster                                                             |
| mako                    | 10.7 ms                                                                | 10.6 ms: 1.00x faster                                                             |
| pidigits                | 197 ms                                                                 | 197 ms: 1.00x slower                                                              |
| 2to3                    | 271 ms                                                                 | 272 ms: 1.00x slower                                                              |
| dulwich_log             | 68.3 ms                                                                | 68.5 ms: 1.00x slower                                                             |
| regex_v8                | 22.1 ms                                                                | 22.2 ms: 1.00x slower                                                             |
| regex_compile           | 145 ms                                                                 | 146 ms: 1.00x slower                                                              |
| bench_thread_pool       | 838 us                                                                 | 842 us: 1.01x slower                                                              |
| sqlglot_normalize       | 113 ms                                                                 | 114 ms: 1.01x slower                                                              |
| pathlib                 | 18.5 ms                                                                | 18.6 ms: 1.01x slower                                                             |
| xml_etree_generate      | 84.7 ms                                                                | 85.1 ms: 1.01x slower                                                             |
| mypy2                   | 351 ms                                                                 | 353 ms: 1.01x slower                                                              |
| tornado_http            | 99.5 ms                                                                | 100 ms: 1.01x slower                                                              |
| asyncio_tcp             | 506 ms                                                                 | 510 ms: 1.01x slower                                                              |
| async_tree_io           | 1.22 sec                                                               | 1.23 sec: 1.01x slower                                                            |
| fannkuch                | 380 ms                                                                 | 383 ms: 1.01x slower                                                              |
| async_generators        | 446 ms                                                                 | 450 ms: 1.01x slower                                                              |
| crypto_pyaes            | 78.0 ms                                                                | 78.7 ms: 1.01x slower                                                             |
| xml_etree_process       | 59.2 ms                                                                | 59.9 ms: 1.01x slower                                                             |
| deepcopy_reduce         | 3.22 us                                                                | 3.26 us: 1.01x slower                                                             |
| unpickle_pure_python    | 219 us                                                                 | 222 us: 1.01x slower                                                              |
| scimark_lu              | 113 ms                                                                 | 115 ms: 1.01x slower                                                              |
| raytrace                | 303 ms                                                                 | 307 ms: 1.01x slower                                                              |
| logging_simple          | 6.34 us                                                                | 6.43 us: 1.01x slower                                                             |
| pickle_list             | 4.50 us                                                                | 4.57 us: 1.02x slower                                                             |
| json_dumps              | 9.98 ms                                                                | 10.1 ms: 1.02x slower                                                             |
| deepcopy                | 368 us                                                                 | 374 us: 1.02x slower                                                              |
| pprint_pformat          | 1.49 sec                                                               | 1.52 sec: 1.02x slower                                                            |
| telco                   | 6.73 ms                                                                | 6.84 ms: 1.02x slower                                                             |
| gc_traversal            | 3.97 ms                                                                | 4.04 ms: 1.02x slower                                                             |
| pycparser               | 1.14 sec                                                               | 1.16 sec: 1.02x slower                                                            |
| pickle                  | 10.5 us                                                                | 10.7 us: 1.02x slower                                                             |
| async_tree_memoization  | 604 ms                                                                 | 616 ms: 1.02x slower                                                              |
| deepcopy_memo           | 38.5 us                                                                | 39.3 us: 1.02x slower                                                             |
| pickle_pure_python      | 313 us                                                                 | 320 us: 1.02x slower                                                              |
| logging_silent          | 101 ns                                                                 | 103 ns: 1.02x slower                                                              |
| pprint_safe_repr        | 732 ms                                                                 | 749 ms: 1.02x slower                                                              |
| regex_dna               | 200 ms                                                                 | 204 ms: 1.02x slower                                                              |
| nbody                   | 87.5 ms                                                                | 90.1 ms: 1.03x slower                                                             |
| go                      | 136 ms                                                                 | 141 ms: 1.04x slower                                                              |
| hexiom                  | 6.18 ms                                                                | 6.43 ms: 1.04x slower                                                             |
| nqueens                 | 80.9 ms                                                                | 84.9 ms: 1.05x slower                                                             |
| meteor_contest          | 113 ms                                                                 | 118 ms: 1.05x slower                                                              |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                                      |

Benchmark hidden because not significant (18): xml_etree_iterparse, xml_etree_parse, sqlglot_transpile, coverage, spectral_norm, chaos, generators, bench_mp_pool, sqlglot_optimize, scimark_sor, logging_format, docutils, deltablue, sqlalchemy_declarative, dask, sqlalchemy_imperative, async_tree_none, async_tree_cpu_io_mixed
