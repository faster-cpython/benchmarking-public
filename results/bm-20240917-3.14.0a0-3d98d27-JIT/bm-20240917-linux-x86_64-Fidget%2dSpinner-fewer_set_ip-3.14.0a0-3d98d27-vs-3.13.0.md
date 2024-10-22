# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: fewer_set_ip
- machine: linux-x86_64
- commit hash: 3d98d27
- commit date: 2024-09-17
- overall geometric mean: 1.01x faster
- HPT reliability: 68.18%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 275 ms: 1.04x slower                                                    |
| docutils       | 2.58 sec                                               | 2.96 sec: 1.15x slower                                                  |
| html5lib       | 64.5 ms                                                | 65.6 ms: 1.02x slower                                                   |
| tornado_http   | 91.5 ms                                                | 94.8 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 388 ms: 1.20x faster                                                    |
| async_tree_none            | 354 ms                                                 | 317 ms: 1.12x faster                                                    |
| async_tree_memoization     | 442 ms                                                 | 398 ms: 1.11x faster                                                    |
| async_tree_none_tg         | 320 ms                                                 | 308 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 566 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 552 ms: 1.02x slower                                                    |
| async_tree_io              | 843 ms                                                 | 863 ms: 1.02x slower                                                    |
| asyncio_tcp                | 488 ms                                                 | 500 ms: 1.03x slower                                                    |
| coroutines                 | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                   |
| async_generators           | 433 ms                                                 | 453 ms: 1.05x slower                                                    |
| async_tree_io_tg           | 825 ms                                                 | 877 ms: 1.06x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 69.1 ms: 1.14x faster                                                   |
| nbody          | 85.7 ms                                                | 82.1 ms: 1.04x faster                                                   |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                  | 1.06x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                | 24.5 ms: 1.03x faster                                                   |
| regex_effbot   | 3.88 ms                                                | 4.01 ms: 1.03x slower                                                   |
| regex_dna      | 220 ms                                                 | 228 ms: 1.04x slower                                                    |
| regex_compile  | 131 ms                                                 | 141 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                  | 1.03x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|---------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate  | 87.0 ms                                                | 77.5 ms: 1.12x faster                                                   |
| xml_etree_process   | 60.4 ms                                                | 53.9 ms: 1.12x faster                                                   |
| tomli_loads         | 2.11 sec                                               | 1.90 sec: 1.11x faster                                                  |
| xml_etree_parse     | 156 ms                                                 | 144 ms: 1.08x faster                                                    |
| xml_etree_iterparse | 102 ms                                                 | 97.8 ms: 1.04x faster                                                   |
| json_dumps          | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                   |
| pickle_dict         | 33.2 us                                                | 33.0 us: 1.00x faster                                                   |
| pickle_list         | 5.01 us                                                | 5.02 us: 1.00x slower                                                   |
| pickle              | 11.6 us                                                | 11.6 us: 1.01x slower                                                   |
| pickle_pure_python  | 300 us                                                 | 307 us: 1.02x slower                                                    |
| unpickle_list       | 4.96 us                                                | 5.18 us: 1.04x slower                                                   |
| Geometric mean      | (ref)                                                  | 1.03x faster                                                            |

Benchmark hidden because not significant (3): unpickle, json_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                   |
| python_startup_no_site | 6.99 ms                                                | 7.04 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.80 ms: 1.13x faster                                                   |
| django_template | 34.4 ms                                                | 35.2 ms: 1.02x slower                                                   |
| genshi_text     | 22.9 ms                                                | 24.3 ms: 1.06x slower                                                   |
| genshi_xml      | 50.3 ms                                                | 57.3 ms: 1.14x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 26.7 us: 1.42x faster                                                   |
| deepcopy                   | 352 us                                                 | 267 us: 1.32x faster                                                    |
| scimark_fft                | 369 ms                                                 | 301 ms: 1.23x faster                                                    |
| richards                   | 48.1 ms                                                | 39.5 ms: 1.22x faster                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.14 ms: 1.21x faster                                                   |
| richards_super             | 54.4 ms                                                | 45.0 ms: 1.21x faster                                                   |
| deepcopy_reduce            | 3.17 us                                                | 2.63 us: 1.20x faster                                                   |
| async_tree_memoization_tg  | 465 ms                                                 | 388 ms: 1.20x faster                                                    |
| float                      | 78.5 ms                                                | 69.1 ms: 1.14x faster                                                   |
| mako                       | 11.1 ms                                                | 9.80 ms: 1.13x faster                                                   |
| xml_etree_generate         | 87.0 ms                                                | 77.5 ms: 1.12x faster                                                   |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.12x faster                                                    |
| xml_etree_process          | 60.4 ms                                                | 53.9 ms: 1.12x faster                                                   |
| async_tree_none            | 354 ms                                                 | 317 ms: 1.12x faster                                                    |
| crypto_pyaes               | 73.0 ms                                                | 65.4 ms: 1.12x faster                                                   |
| tomli_loads                | 2.11 sec                                               | 1.90 sec: 1.11x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 398 ms: 1.11x faster                                                    |
| go                         | 142 ms                                                 | 131 ms: 1.08x faster                                                    |
| xml_etree_parse            | 156 ms                                                 | 144 ms: 1.08x faster                                                    |
| pathlib                    | 17.1 ms                                                | 15.9 ms: 1.07x faster                                                   |
| scimark_monte_carlo        | 66.3 ms                                                | 61.9 ms: 1.07x faster                                                   |
| mdp                        | 2.74 sec                                               | 2.56 sec: 1.07x faster                                                  |
| telco                      | 8.45 ms                                                | 7.91 ms: 1.07x faster                                                   |
| scimark_lu                 | 115 ms                                                 | 109 ms: 1.06x faster                                                    |
| bpe_tokeniser              | 4.69 sec                                               | 4.43 sec: 1.06x faster                                                  |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.05x faster                                                    |
| nbody                      | 85.7 ms                                                | 82.1 ms: 1.04x faster                                                   |
| xml_etree_iterparse        | 102 ms                                                 | 97.8 ms: 1.04x faster                                                   |
| async_tree_none_tg         | 320 ms                                                 | 308 ms: 1.04x faster                                                    |
| pycparser                  | 1.19 sec                                               | 1.15 sec: 1.04x faster                                                  |
| logging_format             | 6.25 us                                                | 6.05 us: 1.03x faster                                                   |
| regex_v8                   | 25.3 ms                                                | 24.5 ms: 1.03x faster                                                   |
| fannkuch                   | 381 ms                                                 | 369 ms: 1.03x faster                                                    |
| logging_simple             | 5.66 us                                                | 5.52 us: 1.03x faster                                                   |
| pyflate                    | 460 ms                                                 | 448 ms: 1.03x faster                                                    |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.02x faster                                                    |
| gc_traversal               | 3.81 ms                                                | 3.74 ms: 1.02x faster                                                   |
| thrift                     | 796 us                                                 | 783 us: 1.02x faster                                                    |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 566 ms: 1.01x faster                                                    |
| json                       | 5.20 ms                                                | 5.12 ms: 1.01x faster                                                   |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                   |
| sqlite_synth               | 2.85 us                                                | 2.81 us: 1.01x faster                                                   |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                   |
| pidigits                   | 186 ms                                                 | 185 ms: 1.00x faster                                                    |
| pickle_dict                | 33.2 us                                                | 33.0 us: 1.00x faster                                                   |
| pickle_list                | 5.01 us                                                | 5.02 us: 1.00x slower                                                   |
| comprehensions             | 16.4 us                                                | 16.5 us: 1.00x slower                                                   |
| pickle                     | 11.6 us                                                | 11.6 us: 1.01x slower                                                   |
| python_startup_no_site     | 6.99 ms                                                | 7.04 ms: 1.01x slower                                                   |
| typing_runtime_protocols   | 159 us                                                 | 160 us: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                  |
| coverage                   | 83.7 ms                                                | 85.0 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 552 ms: 1.02x slower                                                    |
| html5lib                   | 64.5 ms                                                | 65.6 ms: 1.02x slower                                                   |
| deltablue                  | 3.15 ms                                                | 3.21 ms: 1.02x slower                                                   |
| pickle_pure_python         | 300 us                                                 | 307 us: 1.02x slower                                                    |
| django_template            | 34.4 ms                                                | 35.2 ms: 1.02x slower                                                   |
| async_tree_io              | 843 ms                                                 | 863 ms: 1.02x slower                                                    |
| asyncio_tcp                | 488 ms                                                 | 500 ms: 1.03x slower                                                    |
| bench_thread_pool          | 815 us                                                 | 836 us: 1.03x slower                                                    |
| regex_effbot               | 3.88 ms                                                | 4.01 ms: 1.03x slower                                                   |
| coroutines                 | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                   |
| tornado_http               | 91.5 ms                                                | 94.8 ms: 1.04x slower                                                   |
| pprint_pformat             | 1.51 sec                                               | 1.57 sec: 1.04x slower                                                  |
| 2to3                       | 265 ms                                                 | 275 ms: 1.04x slower                                                    |
| regex_dna                  | 220 ms                                                 | 228 ms: 1.04x slower                                                    |
| unpickle_list              | 4.96 us                                                | 5.18 us: 1.04x slower                                                   |
| async_generators           | 433 ms                                                 | 453 ms: 1.05x slower                                                    |
| sqlglot_normalize          | 107 ms                                                 | 113 ms: 1.05x slower                                                    |
| nqueens                    | 80.6 ms                                                | 85.0 ms: 1.05x slower                                                   |
| raytrace                   | 262 ms                                                 | 277 ms: 1.06x slower                                                    |
| async_tree_io_tg           | 825 ms                                                 | 877 ms: 1.06x slower                                                    |
| genshi_text                | 22.9 ms                                                | 24.3 ms: 1.06x slower                                                   |
| sqlglot_parse              | 1.27 ms                                                | 1.35 ms: 1.07x slower                                                   |
| regex_compile              | 131 ms                                                 | 141 ms: 1.07x slower                                                    |
| sqlglot_transpile          | 1.57 ms                                                | 1.69 ms: 1.07x slower                                                   |
| sqlglot_optimize           | 53.9 ms                                                | 57.9 ms: 1.07x slower                                                   |
| dulwich_log                | 63.0 ms                                                | 67.8 ms: 1.08x slower                                                   |
| sympy_str                  | 274 ms                                                 | 295 ms: 1.08x slower                                                    |
| sympy_expand               | 462 ms                                                 | 499 ms: 1.08x slower                                                    |
| create_gc_cycles           | 1.61 ms                                                | 1.75 ms: 1.09x slower                                                   |
| hexiom                     | 6.13 ms                                                | 6.84 ms: 1.12x slower                                                   |
| sympy_integrate            | 19.9 ms                                                | 22.6 ms: 1.14x slower                                                   |
| genshi_xml                 | 50.3 ms                                                | 57.3 ms: 1.14x slower                                                   |
| sympy_sum                  | 150 ms                                                 | 170 ms: 1.14x slower                                                    |
| docutils                   | 2.58 sec                                               | 2.96 sec: 1.15x slower                                                  |
| generators                 | 28.8 ms                                                | 33.3 ms: 1.16x slower                                                   |
| pylint                     | 313 ms                                                 | 371 ms: 1.19x slower                                                    |
| unpack_sequence            | 42.4 ns                                                | 113 ns: 2.66x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (8): unpickle, logging_silent, pprint_safe_repr, asyncio_websockets, json_loads, bench_mp_pool, unpickle_pure_python, chaos
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 68.18% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x