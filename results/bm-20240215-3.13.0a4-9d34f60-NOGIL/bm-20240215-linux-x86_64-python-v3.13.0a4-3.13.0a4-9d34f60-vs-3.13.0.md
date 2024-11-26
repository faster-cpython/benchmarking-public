# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.110x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 296 ms: 1.11x slower                                       |
| chameleon      | 6.94 ms                                                | 8.24 ms: 1.19x slower                                      |
| docutils       | 2.59 sec                                               | 3.07 sec: 1.18x slower                                     |
| html5lib       | 64.2 ms                                                | 67.9 ms: 1.06x slower                                      |
| tornado_http   | 92.4 ms                                                | 98.6 ms: 1.07x slower                                      |
| Geometric mean | (ref)                                                  | 1.12x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_io              | 842 ms                                                 | 796 ms: 1.06x faster                                       |
| async_tree_io_tg           | 857 ms                                                 | 828 ms: 1.03x faster                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 458 ms: 1.01x faster                                       |
| asyncio_websockets         | 552 ms                                                 | 557 ms: 1.01x slower                                       |
| coroutines                 | 22.7 ms                                                | 23.0 ms: 1.01x slower                                      |
| async_generators           | 436 ms                                                 | 463 ms: 1.06x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 476 ms: 1.08x slower                                       |
| async_tree_none            | 351 ms                                                 | 377 ms: 1.08x slower                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 646 ms: 1.12x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 612 ms: 1.12x slower                                       |
| async_tree_none_tg         | 321 ms                                                 | 377 ms: 1.18x slower                                       |
| Geometric mean             | (ref)                                                  | 1.05x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 79.2 ms                                                | 74.2 ms: 1.07x faster                                      |
| pidigits       | 186 ms                                                 | 194 ms: 1.04x slower                                       |
| nbody          | 87.0 ms                                                | 104 ms: 1.20x slower                                       |
| Geometric mean | (ref)                                                  | 1.05x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.1 ms: 1.04x faster                                      |
| regex_effbot   | 3.73 ms                                                | 3.60 ms: 1.04x faster                                      |
| regex_dna      | 218 ms                                                 | 232 ms: 1.06x slower                                       |
| regex_compile  | 132 ms                                                 | 141 ms: 1.06x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| xml_etree_parse      | 156 ms                                                 | 151 ms: 1.03x faster                                       |
| xml_etree_generate   | 86.7 ms                                                | 90.5 ms: 1.04x slower                                      |
| tomli_loads          | 2.14 sec                                               | 2.23 sec: 1.04x slower                                     |
| pickle_pure_python   | 310 us                                                 | 333 us: 1.07x slower                                       |
| json_dumps           | 10.6 ms                                                | 11.6 ms: 1.10x slower                                      |
| unpickle_pure_python | 216 us                                                 | 237 us: 1.10x slower                                       |
| xml_etree_process    | 60.6 ms                                                | 71.1 ms: 1.17x slower                                      |
| json_loads           | 27.2 us                                                | 32.2 us: 1.18x slower                                      |
| xml_etree_iterparse  | 101 ms                                                 | 166 ms: 1.64x slower                                       |
| Geometric mean       | (ref)                                                  | 1.13x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 12.0 ms: 1.04x faster                                      |
| python_startup_no_site | 6.96 ms                                                | 10.0 ms: 1.44x slower                                      |
| Geometric mean         | (ref)                                                  | 1.18x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_xml      | 50.9 ms                                                | 54.7 ms: 1.07x slower                                      |
| genshi_text     | 23.5 ms                                                | 26.1 ms: 1.11x slower                                      |
| django_template | 35.2 ms                                                | 39.1 ms: 1.11x slower                                      |
| mako            | 11.1 ms                                                | 16.3 ms: 1.47x slower                                      |
| Geometric mean  | (ref)                                                  | 1.18x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles           | 2.41 ms                                                | 1.03 ms: 2.34x faster                                      |
| gc_traversal               | 4.37 ms                                                | 2.57 ms: 1.70x faster                                      |
| mypy2                      | 1.04 sec                                               | 696 ms: 1.50x faster                                       |
| typing_runtime_protocols   | 165 us                                                 | 122 us: 1.35x faster                                       |
| float                      | 79.2 ms                                                | 74.2 ms: 1.07x faster                                      |
| async_tree_io              | 842 ms                                                 | 796 ms: 1.06x faster                                       |
| pylint                     | 313 ms                                                 | 296 ms: 1.06x faster                                       |
| regex_v8                   | 26.2 ms                                                | 25.1 ms: 1.04x faster                                      |
| python_startup             | 12.5 ms                                                | 12.0 ms: 1.04x faster                                      |
| regex_effbot               | 3.73 ms                                                | 3.60 ms: 1.04x faster                                      |
| async_tree_io_tg           | 857 ms                                                 | 828 ms: 1.03x faster                                       |
| xml_etree_parse            | 156 ms                                                 | 151 ms: 1.03x faster                                       |
| bench_mp_pool              | 24.0 ms                                                | 23.4 ms: 1.02x faster                                      |
| async_tree_memoization_tg  | 464 ms                                                 | 458 ms: 1.01x faster                                       |
| pycparser                  | 1.20 sec                                               | 1.19 sec: 1.01x faster                                     |
| pyflate                    | 471 ms                                                 | 474 ms: 1.01x slower                                       |
| asyncio_websockets         | 552 ms                                                 | 557 ms: 1.01x slower                                       |
| richards                   | 48.7 ms                                                | 49.2 ms: 1.01x slower                                      |
| coroutines                 | 22.7 ms                                                | 23.0 ms: 1.01x slower                                      |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.02x slower                                       |
| richards_super             | 54.9 ms                                                | 56.3 ms: 1.03x slower                                      |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 5.25 ms: 1.04x slower                                      |
| pidigits                   | 186 ms                                                 | 194 ms: 1.04x slower                                       |
| scimark_fft                | 364 ms                                                 | 380 ms: 1.04x slower                                       |
| xml_etree_generate         | 86.7 ms                                                | 90.5 ms: 1.04x slower                                      |
| tomli_loads                | 2.14 sec                                               | 2.23 sec: 1.04x slower                                     |
| scimark_sor                | 124 ms                                                 | 129 ms: 1.05x slower                                       |
| html5lib                   | 64.2 ms                                                | 67.9 ms: 1.06x slower                                      |
| fannkuch                   | 404 ms                                                 | 428 ms: 1.06x slower                                       |
| meteor_contest             | 109 ms                                                 | 115 ms: 1.06x slower                                       |
| regex_dna                  | 218 ms                                                 | 232 ms: 1.06x slower                                       |
| async_generators           | 436 ms                                                 | 463 ms: 1.06x slower                                       |
| telco                      | 8.54 ms                                                | 9.09 ms: 1.06x slower                                      |
| regex_compile              | 132 ms                                                 | 141 ms: 1.06x slower                                       |
| tornado_http               | 92.4 ms                                                | 98.6 ms: 1.07x slower                                      |
| scimark_lu                 | 113 ms                                                 | 121 ms: 1.07x slower                                       |
| go                         | 144 ms                                                 | 154 ms: 1.07x slower                                       |
| pickle_pure_python         | 310 us                                                 | 333 us: 1.07x slower                                       |
| dulwich_log                | 64.3 ms                                                | 69.0 ms: 1.07x slower                                      |
| hexiom                     | 6.16 ms                                                | 6.62 ms: 1.07x slower                                      |
| genshi_xml                 | 50.9 ms                                                | 54.7 ms: 1.07x slower                                      |
| async_tree_memoization     | 442 ms                                                 | 476 ms: 1.08x slower                                       |
| async_tree_none            | 351 ms                                                 | 377 ms: 1.08x slower                                       |
| sqlglot_normalize          | 108 ms                                                 | 116 ms: 1.08x slower                                       |
| generators                 | 29.0 ms                                                | 31.2 ms: 1.08x slower                                      |
| nqueens                    | 78.4 ms                                                | 84.7 ms: 1.08x slower                                      |
| deepcopy_reduce            | 3.20 us                                                | 3.46 us: 1.08x slower                                      |
| pathlib                    | 17.5 ms                                                | 19.0 ms: 1.08x slower                                      |
| json                       | 5.36 ms                                                | 5.81 ms: 1.08x slower                                      |
| deepcopy                   | 358 us                                                 | 390 us: 1.09x slower                                       |
| pprint_safe_repr           | 728 ms                                                 | 797 ms: 1.09x slower                                       |
| json_dumps                 | 10.6 ms                                                | 11.6 ms: 1.10x slower                                      |
| scimark_monte_carlo        | 67.4 ms                                                | 74.0 ms: 1.10x slower                                      |
| unpickle_pure_python       | 216 us                                                 | 237 us: 1.10x slower                                       |
| pprint_pformat             | 1.49 sec                                               | 1.64 sec: 1.10x slower                                     |
| sqlglot_optimize           | 53.7 ms                                                | 59.3 ms: 1.10x slower                                      |
| genshi_text                | 23.5 ms                                                | 26.1 ms: 1.11x slower                                      |
| 2to3                       | 267 ms                                                 | 296 ms: 1.11x slower                                       |
| django_template            | 35.2 ms                                                | 39.1 ms: 1.11x slower                                      |
| raytrace                   | 267 ms                                                 | 298 ms: 1.12x slower                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 646 ms: 1.12x slower                                       |
| logging_silent             | 102 ns                                                 | 114 ns: 1.12x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 612 ms: 1.12x slower                                       |
| logging_format             | 6.40 us                                                | 7.18 us: 1.12x slower                                      |
| logging_simple             | 5.72 us                                                | 6.43 us: 1.12x slower                                      |
| comprehensions             | 16.5 us                                                | 18.5 us: 1.13x slower                                      |
| sqlglot_transpile          | 1.58 ms                                                | 1.78 ms: 1.13x slower                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.44 ms: 1.13x slower                                      |
| chaos                      | 58.1 ms                                                | 66.2 ms: 1.14x slower                                      |
| deepcopy_memo              | 39.1 us                                                | 45.6 us: 1.17x slower                                      |
| xml_etree_process          | 60.6 ms                                                | 71.1 ms: 1.17x slower                                      |
| async_tree_none_tg         | 321 ms                                                 | 377 ms: 1.18x slower                                       |
| json_loads                 | 27.2 us                                                | 32.2 us: 1.18x slower                                      |
| docutils                   | 2.59 sec                                               | 3.07 sec: 1.18x slower                                     |
| chameleon                  | 6.94 ms                                                | 8.24 ms: 1.19x slower                                      |
| sympy_integrate            | 19.9 ms                                                | 23.8 ms: 1.20x slower                                      |
| nbody                      | 87.0 ms                                                | 104 ms: 1.20x slower                                       |
| sympy_str                  | 275 ms                                                 | 354 ms: 1.29x slower                                       |
| deltablue                  | 3.23 ms                                                | 4.16 ms: 1.29x slower                                      |
| mdp                        | 2.72 sec                                               | 3.64 sec: 1.34x slower                                     |
| sympy_expand               | 463 ms                                                 | 623 ms: 1.34x slower                                       |
| sympy_sum                  | 150 ms                                                 | 211 ms: 1.40x slower                                       |
| python_startup_no_site     | 6.96 ms                                                | 10.0 ms: 1.44x slower                                      |
| mako                       | 11.1 ms                                                | 16.3 ms: 1.47x slower                                      |
| xml_etree_iterparse        | 101 ms                                                 | 166 ms: 1.64x slower                                       |
| bench_thread_pool          | 822 us                                                 | 2.42 ms: 2.95x slower                                      |
| coverage                   | 84.0 ms                                                | 712 ms: 8.48x slower                                       |
| thrift                     | 809 us                                                 | 9.43 ms: 11.65x slower                                     |
| Geometric mean             | (ref)                                                  | 1.13x slower                                               |

Benchmark hidden because not significant (1): crypto_pyaes
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (11) of results/bm-20240215-3.13.0a4-9d34f60-NOGIL/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.110x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: 0.98x