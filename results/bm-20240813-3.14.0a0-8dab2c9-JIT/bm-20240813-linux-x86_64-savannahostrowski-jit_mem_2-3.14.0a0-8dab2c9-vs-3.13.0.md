# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_mem_2
- machine: linux-x86_64
- commit hash: 8dab2c9
- commit date: 2024-08-13
- overall geometric mean: 1.01x faster
- HPT reliability: 52.17%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 284 ms: 1.07x slower                                                  |
| docutils       | 2.58 sec                                               | 2.98 sec: 1.15x slower                                                |
| html5lib       | 64.5 ms                                                | 67.4 ms: 1.04x slower                                                 |
| tornado_http   | 91.5 ms                                                | 94.1 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 395 ms: 1.18x faster                                                  |
| async_tree_none            | 354 ms                                                 | 331 ms: 1.07x faster                                                  |
| async_tree_none_tg         | 320 ms                                                 | 306 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 535 ms: 1.02x faster                                                  |
| coroutines                 | 22.5 ms                                                | 22.7 ms: 1.01x slower                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                |
| asyncio_tcp                | 488 ms                                                 | 503 ms: 1.03x slower                                                  |
| async_generators           | 433 ms                                                 | 447 ms: 1.03x slower                                                  |
| async_tree_io_tg           | 825 ms                                                 | 869 ms: 1.05x slower                                                  |
| async_tree_io              | 843 ms                                                 | 914 ms: 1.08x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 85.7 ms                                                | 80.0 ms: 1.07x faster                                                 |
| float          | 78.5 ms                                                | 73.9 ms: 1.06x faster                                                 |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.59 ms: 1.08x faster                                                 |
| regex_v8       | 25.3 ms                                                | 24.0 ms: 1.06x faster                                                 |
| regex_dna      | 220 ms                                                 | 215 ms: 1.02x faster                                                  |
| regex_compile  | 131 ms                                                 | 142 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|---------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads         | 2.11 sec                                               | 1.90 sec: 1.11x faster                                                |
| xml_etree_process   | 60.4 ms                                                | 58.8 ms: 1.03x faster                                                 |
| xml_etree_generate  | 87.0 ms                                                | 84.9 ms: 1.02x faster                                                 |
| xml_etree_parse     | 156 ms                                                 | 153 ms: 1.02x faster                                                  |
| json_dumps          | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| xml_etree_iterparse | 102 ms                                                 | 101 ms: 1.01x faster                                                  |
| pickle_pure_python  | 300 us                                                 | 305 us: 1.01x slower                                                  |
| json_loads          | 27.0 us                                                | 28.4 us: 1.05x slower                                                 |
| Geometric mean      | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.4 ms: 1.01x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 7.09 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.87 ms: 1.12x faster                                                 |
| django_template | 34.4 ms                                                | 37.0 ms: 1.07x slower                                                 |
| genshi_text     | 22.9 ms                                                | 25.2 ms: 1.10x slower                                                 |
| genshi_xml      | 50.3 ms                                                | 56.6 ms: 1.12x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 27.3 us: 1.39x faster                                                 |
| deepcopy                   | 352 us                                                 | 269 us: 1.31x faster                                                  |
| scimark_fft                | 369 ms                                                 | 306 ms: 1.21x faster                                                  |
| deepcopy_reduce            | 3.17 us                                                | 2.65 us: 1.20x faster                                                 |
| richards_super             | 54.4 ms                                                | 45.6 ms: 1.19x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.23 ms: 1.19x faster                                                 |
| richards                   | 48.1 ms                                                | 40.5 ms: 1.19x faster                                                 |
| async_tree_memoization_tg  | 465 ms                                                 | 395 ms: 1.18x faster                                                  |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.13x faster                                                  |
| mako                       | 11.1 ms                                                | 9.87 ms: 1.12x faster                                                 |
| tomli_loads                | 2.11 sec                                               | 1.90 sec: 1.11x faster                                                |
| gc_traversal               | 3.81 ms                                                | 3.48 ms: 1.09x faster                                                 |
| crypto_pyaes               | 73.0 ms                                                | 67.3 ms: 1.08x faster                                                 |
| telco                      | 8.45 ms                                                | 7.82 ms: 1.08x faster                                                 |
| regex_effbot               | 3.88 ms                                                | 3.59 ms: 1.08x faster                                                 |
| nbody                      | 85.7 ms                                                | 80.0 ms: 1.07x faster                                                 |
| async_tree_none            | 354 ms                                                 | 331 ms: 1.07x faster                                                  |
| mdp                        | 2.74 sec                                               | 2.56 sec: 1.07x faster                                                |
| float                      | 78.5 ms                                                | 73.9 ms: 1.06x faster                                                 |
| pathlib                    | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                 |
| scimark_sor                | 122 ms                                                 | 115 ms: 1.06x faster                                                  |
| pyflate                    | 460 ms                                                 | 434 ms: 1.06x faster                                                  |
| scimark_monte_carlo        | 66.3 ms                                                | 62.6 ms: 1.06x faster                                                 |
| regex_v8                   | 25.3 ms                                                | 24.0 ms: 1.06x faster                                                 |
| scimark_lu                 | 115 ms                                                 | 110 ms: 1.05x faster                                                  |
| async_tree_none_tg         | 320 ms                                                 | 306 ms: 1.05x faster                                                  |
| fannkuch                   | 381 ms                                                 | 369 ms: 1.03x faster                                                  |
| meteor_contest             | 108 ms                                                 | 104 ms: 1.03x faster                                                  |
| xml_etree_process          | 60.4 ms                                                | 58.8 ms: 1.03x faster                                                 |
| logging_format             | 6.25 us                                                | 6.10 us: 1.03x faster                                                 |
| xml_etree_generate         | 87.0 ms                                                | 84.9 ms: 1.02x faster                                                 |
| pycparser                  | 1.19 sec                                               | 1.17 sec: 1.02x faster                                                |
| regex_dna                  | 220 ms                                                 | 215 ms: 1.02x faster                                                  |
| logging_simple             | 5.66 us                                                | 5.54 us: 1.02x faster                                                 |
| xml_etree_parse            | 156 ms                                                 | 153 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 535 ms: 1.02x faster                                                  |
| python_startup             | 10.6 ms                                                | 10.4 ms: 1.01x faster                                                 |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| xml_etree_iterparse        | 102 ms                                                 | 101 ms: 1.01x faster                                                  |
| deltablue                  | 3.15 ms                                                | 3.13 ms: 1.00x faster                                                 |
| pidigits                   | 186 ms                                                 | 185 ms: 1.00x faster                                                  |
| bench_thread_pool          | 815 us                                                 | 821 us: 1.01x slower                                                  |
| comprehensions             | 16.4 us                                                | 16.5 us: 1.01x slower                                                 |
| coroutines                 | 22.5 ms                                                | 22.7 ms: 1.01x slower                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                |
| coverage                   | 83.7 ms                                                | 84.8 ms: 1.01x slower                                                 |
| python_startup_no_site     | 6.99 ms                                                | 7.09 ms: 1.01x slower                                                 |
| pickle_pure_python         | 300 us                                                 | 305 us: 1.01x slower                                                  |
| tornado_http               | 91.5 ms                                                | 94.1 ms: 1.03x slower                                                 |
| asyncio_tcp                | 488 ms                                                 | 503 ms: 1.03x slower                                                  |
| pprint_pformat             | 1.51 sec                                               | 1.56 sec: 1.03x slower                                                |
| raytrace                   | 262 ms                                                 | 270 ms: 1.03x slower                                                  |
| async_generators           | 433 ms                                                 | 447 ms: 1.03x slower                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.86 sec: 1.04x slower                                                |
| html5lib                   | 64.5 ms                                                | 67.4 ms: 1.04x slower                                                 |
| go                         | 142 ms                                                 | 148 ms: 1.05x slower                                                  |
| json_loads                 | 27.0 us                                                | 28.4 us: 1.05x slower                                                 |
| sqlglot_parse              | 1.27 ms                                                | 1.33 ms: 1.05x slower                                                 |
| async_tree_io_tg           | 825 ms                                                 | 869 ms: 1.05x slower                                                  |
| sqlglot_normalize          | 107 ms                                                 | 113 ms: 1.05x slower                                                  |
| json                       | 5.20 ms                                                | 5.50 ms: 1.06x slower                                                 |
| sqlglot_transpile          | 1.57 ms                                                | 1.69 ms: 1.07x slower                                                 |
| 2to3                       | 265 ms                                                 | 284 ms: 1.07x slower                                                  |
| django_template            | 34.4 ms                                                | 37.0 ms: 1.07x slower                                                 |
| create_gc_cycles           | 1.61 ms                                                | 1.73 ms: 1.08x slower                                                 |
| typing_runtime_protocols   | 159 us                                                 | 172 us: 1.08x slower                                                  |
| sqlglot_optimize           | 53.9 ms                                                | 58.3 ms: 1.08x slower                                                 |
| sympy_str                  | 274 ms                                                 | 296 ms: 1.08x slower                                                  |
| regex_compile              | 131 ms                                                 | 142 ms: 1.08x slower                                                  |
| async_tree_io              | 843 ms                                                 | 914 ms: 1.08x slower                                                  |
| nqueens                    | 80.6 ms                                                | 87.8 ms: 1.09x slower                                                 |
| sympy_expand               | 462 ms                                                 | 505 ms: 1.09x slower                                                  |
| genshi_text                | 22.9 ms                                                | 25.2 ms: 1.10x slower                                                 |
| hexiom                     | 6.13 ms                                                | 6.80 ms: 1.11x slower                                                 |
| genshi_xml                 | 50.3 ms                                                | 56.6 ms: 1.12x slower                                                 |
| sympy_sum                  | 150 ms                                                 | 170 ms: 1.13x slower                                                  |
| sympy_integrate            | 19.9 ms                                                | 22.8 ms: 1.15x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.98 sec: 1.15x slower                                                |
| pylint                     | 313 ms                                                 | 366 ms: 1.17x slower                                                  |
| generators                 | 28.8 ms                                                | 35.4 ms: 1.23x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (9): async_tree_memoization, async_tree_cpu_io_mixed, chaos, thrift, bench_mp_pool, pprint_safe_repr, asyncio_websockets, unpickle_pure_python, logging_silent
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 52.17% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x