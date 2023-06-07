
# Results vs. base

- fork: mdboom
- ref: match_nogil_immortal
- machine: linux-x86_64
- commit hash: 82b39b9
- commit date: 2023-06-07
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230422-linux-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 | bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7+-82b39b9 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                                 | 260 ms: 1.02x faster                                                   |
| chameleon      | 6.84 ms                                                                | 6.91 ms: 1.01x slower                                                  |
| docutils       | 2.69 sec                                                               | 2.35 sec: 1.14x faster                                                 |
| html5lib       | 64.6 ms                                                                | 62.9 ms: 1.03x faster                                                  |
| tornado_http   | 105 ms                                                                 | 102 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                                  | 1.04x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230422-linux-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 | bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7+-82b39b9 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 79.4 ms                                                                | 69.2 ms: 1.15x faster                                                  |
| nbody          | 88.8 ms                                                                | 91.3 ms: 1.03x slower                                                  |
| pidigits       | 189 ms                                                                 | 197 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230422-linux-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 | bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7+-82b39b9 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 22.3 ms                                                                | 21.9 ms: 1.02x faster                                                  |
| regex_effbot   | 3.32 ms                                                                | 3.38 ms: 1.02x slower                                                  |
| regex_compile  | 143 ms                                                                 | 146 ms: 1.02x slower                                                   |
| regex_dna      | 204 ms                                                                 | 209 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230422-linux-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 | bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7+-82b39b9 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 104 ms                                                                 | 79.5 ms: 1.30x faster                                                  |
| xml_etree_parse      | 155 ms                                                                 | 124 ms: 1.25x faster                                                   |
| unpickle_list        | 5.41 us                                                                | 5.09 us: 1.06x faster                                                  |
| xml_etree_generate   | 83.3 ms                                                                | 78.4 ms: 1.06x faster                                                  |
| pickle_dict          | 31.7 us                                                                | 29.9 us: 1.06x faster                                                  |
| xml_etree_process    | 58.5 ms                                                                | 56.6 ms: 1.03x faster                                                  |
| pickle               | 10.4 us                                                                | 10.3 us: 1.01x faster                                                  |
| pickle_list          | 4.43 us                                                                | 4.36 us: 1.01x faster                                                  |
| json_dumps           | 9.74 ms                                                                | 9.70 ms: 1.00x faster                                                  |
| unpickle             | 14.6 us                                                                | 14.5 us: 1.00x faster                                                  |
| pickle_pure_python   | 308 us                                                                 | 314 us: 1.02x slower                                                   |
| unpickle_pure_python | 213 us                                                                 | 218 us: 1.02x slower                                                   |
| Geometric mean       | (ref)                                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230422-linux-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 | bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7+-82b39b9 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.64 ms                                                                | 6.46 ms: 1.03x faster                                                  |
| python_startup         | 9.04 ms                                                                | 8.83 ms: 1.02x faster                                                  |
| Geometric mean         | (ref)                                                                  | 1.03x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230422-linux-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 | bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7+-82b39b9 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 50.0 ms                                                                | 49.2 ms: 1.02x faster                                                  |
| mako            | 10.5 ms                                                                | 10.6 ms: 1.01x slower                                                  |
| genshi_text     | 22.5 ms                                                                | 23.0 ms: 1.02x slower                                                  |
| django_template | 34.3 ms                                                                | 35.6 ms: 1.04x slower                                                  |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                           |

All benchmarks:
===============

| Benchmark               | bm-20230422-linux-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 | bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7+-82b39b9 |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.30 sec                                                               | 523 ms: 2.48x faster                                                   |
| async_tree_memoization  | 661 ms                                                                 | 318 ms: 2.08x faster                                                   |
| async_tree_none         | 529 ms                                                                 | 262 ms: 2.02x faster                                                   |
| async_tree_cpu_io_mixed | 746 ms                                                                 | 469 ms: 1.59x faster                                                   |
| xml_etree_iterparse     | 104 ms                                                                 | 79.5 ms: 1.30x faster                                                  |
| xml_etree_parse         | 155 ms                                                                 | 124 ms: 1.25x faster                                                   |
| float                   | 79.4 ms                                                                | 69.2 ms: 1.15x faster                                                  |
| docutils                | 2.69 sec                                                               | 2.35 sec: 1.14x faster                                                 |
| pycparser               | 1.14 sec                                                               | 1.05 sec: 1.09x faster                                                 |
| dask                    | 538 ms                                                                 | 500 ms: 1.08x faster                                                   |
| mypy2                   | 360 ms                                                                 | 337 ms: 1.07x faster                                                   |
| async_generators        | 438 ms                                                                 | 411 ms: 1.06x faster                                                   |
| unpickle_list           | 5.41 us                                                                | 5.09 us: 1.06x faster                                                  |
| xml_etree_generate      | 83.3 ms                                                                | 78.4 ms: 1.06x faster                                                  |
| pylint                  | 468 ms                                                                 | 441 ms: 1.06x faster                                                   |
| pickle_dict             | 31.7 us                                                                | 29.9 us: 1.06x faster                                                  |
| sqlalchemy_imperative   | 19.8 ms                                                                | 18.8 ms: 1.05x faster                                                  |
| sqlalchemy_declarative  | 147 ms                                                                 | 140 ms: 1.05x faster                                                   |
| gc_traversal            | 3.84 ms                                                                | 3.72 ms: 1.03x faster                                                  |
| xml_etree_process       | 58.5 ms                                                                | 56.6 ms: 1.03x faster                                                  |
| html5lib                | 64.6 ms                                                                | 62.9 ms: 1.03x faster                                                  |
| python_startup_no_site  | 6.64 ms                                                                | 6.46 ms: 1.03x faster                                                  |
| python_startup          | 9.04 ms                                                                | 8.83 ms: 1.02x faster                                                  |
| 2to3                    | 266 ms                                                                 | 260 ms: 1.02x faster                                                   |
| tornado_http            | 105 ms                                                                 | 102 ms: 1.02x faster                                                   |
| scimark_sparse_mat_mult | 4.70 ms                                                                | 4.62 ms: 1.02x faster                                                  |
| sympy_str               | 315 ms                                                                 | 310 ms: 1.02x faster                                                   |
| regex_v8                | 22.3 ms                                                                | 21.9 ms: 1.02x faster                                                  |
| scimark_lu              | 112 ms                                                                 | 110 ms: 1.02x faster                                                   |
| genshi_xml              | 50.0 ms                                                                | 49.2 ms: 1.02x faster                                                  |
| pickle                  | 10.4 us                                                                | 10.3 us: 1.01x faster                                                  |
| pickle_list             | 4.43 us                                                                | 4.36 us: 1.01x faster                                                  |
| sqlglot_parse           | 1.31 ms                                                                | 1.29 ms: 1.01x faster                                                  |
| sqlglot_transpile       | 1.63 ms                                                                | 1.61 ms: 1.01x faster                                                  |
| pathlib                 | 17.9 ms                                                                | 17.7 ms: 1.01x faster                                                  |
| sympy_expand            | 500 ms                                                                 | 495 ms: 1.01x faster                                                   |
| pprint_pformat          | 1.51 sec                                                               | 1.49 sec: 1.01x faster                                                 |
| dulwich_log             | 68.1 ms                                                                | 67.5 ms: 1.01x faster                                                  |
| mdp                     | 2.58 sec                                                               | 2.56 sec: 1.01x faster                                                 |
| pprint_safe_repr        | 738 ms                                                                 | 732 ms: 1.01x faster                                                   |
| deltablue               | 3.57 ms                                                                | 3.55 ms: 1.01x faster                                                  |
| sympy_sum               | 181 ms                                                                 | 180 ms: 1.01x faster                                                   |
| json_dumps              | 9.74 ms                                                                | 9.70 ms: 1.00x faster                                                  |
| nqueens                 | 80.7 ms                                                                | 80.5 ms: 1.00x faster                                                  |
| unpickle                | 14.6 us                                                                | 14.5 us: 1.00x faster                                                  |
| deepcopy                | 359 us                                                                 | 361 us: 1.01x slower                                                   |
| comprehensions          | 23.2 us                                                                | 23.4 us: 1.01x slower                                                  |
| scimark_monte_carlo     | 72.0 ms                                                                | 72.5 ms: 1.01x slower                                                  |
| fannkuch                | 387 ms                                                                 | 390 ms: 1.01x slower                                                   |
| sqlglot_normalize       | 111 ms                                                                 | 112 ms: 1.01x slower                                                   |
| meteor_contest          | 113 ms                                                                 | 114 ms: 1.01x slower                                                   |
| pyflate                 | 455 ms                                                                 | 459 ms: 1.01x slower                                                   |
| chameleon               | 6.84 ms                                                                | 6.91 ms: 1.01x slower                                                  |
| deepcopy_reduce         | 3.17 us                                                                | 3.20 us: 1.01x slower                                                  |
| logging_format          | 6.93 us                                                                | 7.00 us: 1.01x slower                                                  |
| mako                    | 10.5 ms                                                                | 10.6 ms: 1.01x slower                                                  |
| generators              | 30.4 ms                                                                | 30.7 ms: 1.01x slower                                                  |
| bench_thread_pool       | 834 us                                                                 | 846 us: 1.01x slower                                                   |
| hexiom                  | 6.25 ms                                                                | 6.34 ms: 1.01x slower                                                  |
| create_gc_cycles        | 1.51 ms                                                                | 1.53 ms: 1.01x slower                                                  |
| sqlglot_optimize        | 54.2 ms                                                                | 55.1 ms: 1.02x slower                                                  |
| scimark_fft             | 347 ms                                                                 | 353 ms: 1.02x slower                                                   |
| logging_silent          | 95.9 ns                                                                | 97.5 ns: 1.02x slower                                                  |
| go                      | 136 ms                                                                 | 138 ms: 1.02x slower                                                   |
| regex_effbot            | 3.32 ms                                                                | 3.38 ms: 1.02x slower                                                  |
| pickle_pure_python      | 308 us                                                                 | 314 us: 1.02x slower                                                   |
| json                    | 4.69 ms                                                                | 4.79 ms: 1.02x slower                                                  |
| genshi_text             | 22.5 ms                                                                | 23.0 ms: 1.02x slower                                                  |
| regex_compile           | 143 ms                                                                 | 146 ms: 1.02x slower                                                   |
| regex_dna               | 204 ms                                                                 | 209 ms: 1.02x slower                                                   |
| unpickle_pure_python    | 213 us                                                                 | 218 us: 1.02x slower                                                   |
| asyncio_tcp             | 501 ms                                                                 | 512 ms: 1.02x slower                                                   |
| logging_simple          | 6.16 us                                                                | 6.31 us: 1.02x slower                                                  |
| richards                | 42.9 ms                                                                | 44.0 ms: 1.02x slower                                                  |
| nbody                   | 88.8 ms                                                                | 91.3 ms: 1.03x slower                                                  |
| raytrace                | 296 ms                                                                 | 304 ms: 1.03x slower                                                   |
| thrift                  | 787 us                                                                 | 812 us: 1.03x slower                                                   |
| telco                   | 6.69 ms                                                                | 6.92 ms: 1.03x slower                                                  |
| deepcopy_memo           | 37.5 us                                                                | 38.9 us: 1.04x slower                                                  |
| django_template         | 34.3 ms                                                                | 35.6 ms: 1.04x slower                                                  |
| coverage                | 99.9 ms                                                                | 104 ms: 1.04x slower                                                   |
| pidigits                | 189 ms                                                                 | 197 ms: 1.04x slower                                                   |
| spectral_norm           | 102 ms                                                                 | 106 ms: 1.05x slower                                                   |
| unpack_sequence         | 46.7 ns                                                                | 49.8 ns: 1.07x slower                                                  |
| scimark_sor             | 118 ms                                                                 | 126 ms: 1.07x slower                                                   |
| coroutines              | 21.9 ms                                                                | 23.5 ms: 1.08x slower                                                  |
| Geometric mean          | (ref)                                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (7): djangocms, sqlite_synth, json_loads, sympy_integrate, bench_mp_pool, crypto_pyaes, chaos
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20230607-3.12.0a7+-82b39b9/bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7+-82b39b9.json: aiohttp, asyncio_tcp_ssl, gunicorn, richards_super, tomli_loads, typing_runtime_protocols
