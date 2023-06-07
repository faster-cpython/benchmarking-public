
# Results vs. 3.11.0

- fork: mdboom
- ref: match_nogil_immortal
- machine: linux-x86_64
- commit hash: 82b39b9
- commit date: 2023-06-07
- overall geometric mean: 1.05x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7+-82b39b9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 260 ms: 1.00x slower                                                   |
| chameleon      | 6.47 ms                                                | 6.91 ms: 1.07x slower                                                  |
| docutils       | 2.63 sec                                               | 2.35 sec: 1.12x faster                                                 |
| html5lib       | 64.5 ms                                                | 62.9 ms: 1.03x faster                                                  |
| tornado_http   | 96.3 ms                                                | 102 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7+-82b39b9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 69.2 ms: 1.12x faster                                                  |
| nbody          | 93.1 ms                                                | 91.3 ms: 1.02x faster                                                  |
| pidigits       | 198 ms                                                 | 197 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7+-82b39b9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.38 ms: 1.18x faster                                                  |
| regex_v8       | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                  |
| regex_dna      | 204 ms                                                 | 209 ms: 1.02x slower                                                   |
| regex_compile  | 138 ms                                                 | 146 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7+-82b39b9 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 104 ms                                                 | 79.5 ms: 1.31x faster                                                  |
| json_dumps           | 12.6 ms                                                | 9.70 ms: 1.30x faster                                                  |
| xml_etree_parse      | 158 ms                                                 | 124 ms: 1.28x faster                                                   |
| json_loads           | 26.5 us                                                | 24.9 us: 1.06x faster                                                  |
| unpickle_pure_python | 228 us                                                 | 218 us: 1.04x faster                                                   |
| pickle_dict          | 31.1 us                                                | 29.9 us: 1.04x faster                                                  |
| tomli_loads          | 2.22 sec                                               | 2.18 sec: 1.02x faster                                                 |
| pickle               | 10.1 us                                                | 10.3 us: 1.02x slower                                                  |
| pickle_pure_python   | 306 us                                                 | 314 us: 1.03x slower                                                   |
| xml_etree_generate   | 76.2 ms                                                | 78.4 ms: 1.03x slower                                                  |
| unpickle_list        | 4.91 us                                                | 5.09 us: 1.04x slower                                                  |
| xml_etree_process    | 53.9 ms                                                | 56.6 ms: 1.05x slower                                                  |
| pickle_list          | 4.11 us                                                | 4.36 us: 1.06x slower                                                  |
| unpickle             | 13.7 us                                                | 14.5 us: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7+-82b39b9 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.83 ms: 1.04x slower                                                  |
| python_startup_no_site | 6.01 ms                                                | 6.46 ms: 1.08x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7+-82b39b9 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 49.2 ms: 1.05x faster                                                  |
| mako            | 10.1 ms                                                | 10.6 ms: 1.05x slower                                                  |
| genshi_text     | 21.6 ms                                                | 23.0 ms: 1.07x slower                                                  |
| django_template | 32.6 ms                                                | 35.6 ms: 1.09x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                           |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7+-82b39b9 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io            | 1.30 sec                                               | 523 ms: 2.48x faster                                                   |
| generators               | 73.5 ms                                                | 30.7 ms: 2.39x faster                                                  |
| typing_runtime_protocols | 486 us                                                 | 216 us: 2.25x faster                                                   |
| async_tree_none          | 526 ms                                                 | 262 ms: 2.01x faster                                                   |
| async_tree_memoization   | 627 ms                                                 | 318 ms: 1.97x faster                                                   |
| asyncio_tcp              | 922 ms                                                 | 512 ms: 1.80x faster                                                   |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.80 sec: 1.74x faster                                                 |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 469 ms: 1.57x faster                                                   |
| xml_etree_iterparse      | 104 ms                                                 | 79.5 ms: 1.31x faster                                                  |
| json_dumps               | 12.6 ms                                                | 9.70 ms: 1.30x faster                                                  |
| xml_etree_parse          | 158 ms                                                 | 124 ms: 1.28x faster                                                   |
| mypy2                    | 420 ms                                                 | 337 ms: 1.25x faster                                                   |
| regex_effbot             | 3.99 ms                                                | 3.38 ms: 1.18x faster                                                  |
| pycparser                | 1.18 sec                                               | 1.05 sec: 1.12x faster                                                 |
| docutils                 | 2.63 sec                                               | 2.35 sec: 1.12x faster                                                 |
| float                    | 77.2 ms                                                | 69.2 ms: 1.12x faster                                                  |
| sqlglot_parse            | 1.40 ms                                                | 1.29 ms: 1.09x faster                                                  |
| coroutines               | 25.5 ms                                                | 23.5 ms: 1.08x faster                                                  |
| gc_traversal             | 4.02 ms                                                | 3.72 ms: 1.08x faster                                                  |
| json_loads               | 26.5 us                                                | 24.9 us: 1.06x faster                                                  |
| sqlglot_transpile        | 1.70 ms                                                | 1.61 ms: 1.06x faster                                                  |
| pylint                   | 465 ms                                                 | 441 ms: 1.05x faster                                                   |
| genshi_xml               | 51.8 ms                                                | 49.2 ms: 1.05x faster                                                  |
| unpickle_pure_python     | 228 us                                                 | 218 us: 1.04x faster                                                   |
| pickle_dict              | 31.1 us                                                | 29.9 us: 1.04x faster                                                  |
| richards                 | 45.7 ms                                                | 44.0 ms: 1.04x faster                                                  |
| logging_silent           | 101 ns                                                 | 97.5 ns: 1.04x faster                                                  |
| nqueens                  | 83.4 ms                                                | 80.5 ms: 1.04x faster                                                  |
| deltablue                | 3.67 ms                                                | 3.55 ms: 1.04x faster                                                  |
| json                     | 4.94 ms                                                | 4.79 ms: 1.03x faster                                                  |
| richards_super           | 56.8 ms                                                | 55.0 ms: 1.03x faster                                                  |
| pathlib                  | 18.2 ms                                                | 17.7 ms: 1.03x faster                                                  |
| html5lib                 | 64.5 ms                                                | 62.9 ms: 1.03x faster                                                  |
| mdp                      | 2.62 sec                                               | 2.56 sec: 1.02x faster                                                 |
| nbody                    | 93.1 ms                                                | 91.3 ms: 1.02x faster                                                  |
| chaos                    | 69.2 ms                                                | 68.0 ms: 1.02x faster                                                  |
| tomli_loads              | 2.22 sec                                               | 2.18 sec: 1.02x faster                                                 |
| go                       | 140 ms                                                 | 138 ms: 1.01x faster                                                   |
| pidigits                 | 198 ms                                                 | 197 ms: 1.01x faster                                                   |
| regex_v8                 | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                  |
| hexiom                   | 6.37 ms                                                | 6.34 ms: 1.00x faster                                                  |
| 2to3                     | 259 ms                                                 | 260 ms: 1.00x slower                                                   |
| scimark_lu               | 110 ms                                                 | 110 ms: 1.00x slower                                                   |
| fannkuch                 | 388 ms                                                 | 390 ms: 1.01x slower                                                   |
| sqlalchemy_declarative   | 138 ms                                                 | 140 ms: 1.01x slower                                                   |
| pickle                   | 10.1 us                                                | 10.3 us: 1.02x slower                                                  |
| regex_dna                | 204 ms                                                 | 209 ms: 1.02x slower                                                   |
| pprint_pformat           | 1.46 sec                                               | 1.49 sec: 1.02x slower                                                 |
| pickle_pure_python       | 306 us                                                 | 314 us: 1.03x slower                                                   |
| raytrace                 | 297 ms                                                 | 304 ms: 1.03x slower                                                   |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.62 ms: 1.03x slower                                                  |
| xml_etree_generate       | 76.2 ms                                                | 78.4 ms: 1.03x slower                                                  |
| create_gc_cycles         | 1.49 ms                                                | 1.53 ms: 1.03x slower                                                  |
| djangocms                | 32.4 us                                                | 33.5 us: 1.03x slower                                                  |
| bench_thread_pool        | 819 us                                                 | 846 us: 1.03x slower                                                   |
| python_startup           | 8.52 ms                                                | 8.83 ms: 1.04x slower                                                  |
| sqlglot_normalize        | 108 ms                                                 | 112 ms: 1.04x slower                                                   |
| sqlglot_optimize         | 53.1 ms                                                | 55.1 ms: 1.04x slower                                                  |
| unpickle_list            | 4.91 us                                                | 5.09 us: 1.04x slower                                                  |
| coverage                 | 100 ms                                                 | 104 ms: 1.04x slower                                                   |
| comprehensions           | 22.4 us                                                | 23.4 us: 1.04x slower                                                  |
| sympy_integrate          | 21.0 ms                                                | 21.9 ms: 1.04x slower                                                  |
| sympy_expand             | 475 ms                                                 | 495 ms: 1.04x slower                                                   |
| pprint_safe_repr         | 701 ms                                                 | 732 ms: 1.04x slower                                                   |
| crypto_pyaes             | 74.7 ms                                                | 78.0 ms: 1.04x slower                                                  |
| logging_simple           | 6.03 us                                                | 6.31 us: 1.05x slower                                                  |
| logging_format           | 6.68 us                                                | 7.00 us: 1.05x slower                                                  |
| telco                    | 6.58 ms                                                | 6.92 ms: 1.05x slower                                                  |
| deepcopy_memo            | 37.0 us                                                | 38.9 us: 1.05x slower                                                  |
| xml_etree_process        | 53.9 ms                                                | 56.6 ms: 1.05x slower                                                  |
| mako                     | 10.1 ms                                                | 10.6 ms: 1.05x slower                                                  |
| sqlalchemy_imperative    | 17.9 ms                                                | 18.8 ms: 1.05x slower                                                  |
| deepcopy                 | 342 us                                                 | 361 us: 1.05x slower                                                   |
| aiohttp                  | 1.10 ms                                                | 1.16 ms: 1.06x slower                                                  |
| gunicorn                 | 1.18 ms                                                | 1.25 ms: 1.06x slower                                                  |
| regex_compile            | 138 ms                                                 | 146 ms: 1.06x slower                                                   |
| dulwich_log              | 63.7 ms                                                | 67.5 ms: 1.06x slower                                                  |
| sqlite_synth             | 2.52 us                                                | 2.68 us: 1.06x slower                                                  |
| pickle_list              | 4.11 us                                                | 4.36 us: 1.06x slower                                                  |
| unpickle                 | 13.7 us                                                | 14.5 us: 1.06x slower                                                  |
| tornado_http             | 96.3 ms                                                | 102 ms: 1.06x slower                                                   |
| spectral_norm            | 100 ms                                                 | 106 ms: 1.06x slower                                                   |
| scimark_monte_carlo      | 68.1 ms                                                | 72.5 ms: 1.07x slower                                                  |
| genshi_text              | 21.6 ms                                                | 23.0 ms: 1.07x slower                                                  |
| chameleon                | 6.47 ms                                                | 6.91 ms: 1.07x slower                                                  |
| sympy_str                | 290 ms                                                 | 310 ms: 1.07x slower                                                   |
| meteor_contest           | 107 ms                                                 | 114 ms: 1.07x slower                                                   |
| scimark_sor              | 118 ms                                                 | 126 ms: 1.07x slower                                                   |
| thrift                   | 756 us                                                 | 812 us: 1.07x slower                                                   |
| scimark_fft              | 328 ms                                                 | 353 ms: 1.07x slower                                                   |
| python_startup_no_site   | 6.01 ms                                                | 6.46 ms: 1.08x slower                                                  |
| sympy_sum                | 167 ms                                                 | 180 ms: 1.08x slower                                                   |
| deepcopy_reduce          | 2.94 us                                                | 3.20 us: 1.09x slower                                                  |
| django_template          | 32.6 ms                                                | 35.6 ms: 1.09x slower                                                  |
| pyflate                  | 418 ms                                                 | 459 ms: 1.10x slower                                                   |
| async_generators         | 368 ms                                                 | 411 ms: 1.12x slower                                                   |
| unpack_sequence          | 43.1 ns                                                | 49.8 ns: 1.16x slower                                                  |
| dask                     | 360 ms                                                 | 500 ms: 1.39x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging
