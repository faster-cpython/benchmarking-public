# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.017x slower
- HPT reliability: 99.85%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.88x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 269 ms: 1.01x slower                                       |
| chameleon      | 6.94 ms                                                | 6.85 ms: 1.01x faster                                      |
| docutils       | 2.59 sec                                               | 2.65 sec: 1.02x slower                                     |
| html5lib       | 64.2 ms                                                | 67.4 ms: 1.05x slower                                      |
| tornado_http   | 92.4 ms                                                | 97.1 ms: 1.05x slower                                      |
| Geometric mean | (ref)                                                  | 1.02x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| coroutines                 | 22.7 ms                                                | 23.0 ms: 1.01x slower                                      |
| asyncio_websockets         | 552 ms                                                 | 563 ms: 1.02x slower                                       |
| async_generators           | 436 ms                                                 | 459 ms: 1.05x slower                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 718 ms: 1.25x slower                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 585 ms: 1.26x slower                                       |
| async_tree_none            | 351 ms                                                 | 444 ms: 1.27x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 571 ms: 1.29x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 733 ms: 1.34x slower                                       |
| async_tree_none_tg         | 321 ms                                                 | 455 ms: 1.42x slower                                       |
| async_tree_io              | 842 ms                                                 | 1.20 sec: 1.43x slower                                     |
| async_tree_io_tg           | 857 ms                                                 | 1.22 sec: 1.43x slower                                     |
| Geometric mean             | (ref)                                                  | 1.24x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 189 ms: 1.02x slower                                       |
| float          | 79.2 ms                                                | 83.1 ms: 1.05x slower                                      |
| nbody          | 87.0 ms                                                | 92.1 ms: 1.06x slower                                      |
| Geometric mean | (ref)                                                  | 1.04x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.4 ms: 1.07x faster                                      |
| regex_effbot   | 3.73 ms                                                | 3.66 ms: 1.02x faster                                      |
| regex_compile  | 132 ms                                                 | 132 ms: 1.00x faster                                       |
| regex_dna      | 218 ms                                                 | 224 ms: 1.02x slower                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 310 us                                                 | 302 us: 1.03x faster                                       |
| xml_etree_process    | 60.6 ms                                                | 59.3 ms: 1.02x faster                                      |
| json_dumps           | 10.6 ms                                                | 10.5 ms: 1.01x faster                                      |
| unpickle_pure_python | 216 us                                                 | 217 us: 1.00x slower                                       |
| tomli_loads          | 2.14 sec                                               | 2.20 sec: 1.03x slower                                     |
| json_loads           | 27.2 us                                                | 27.9 us: 1.03x slower                                      |
| xml_etree_parse      | 156 ms                                                 | 160 ms: 1.03x slower                                       |
| xml_etree_iterparse  | 101 ms                                                 | 107 ms: 1.06x slower                                       |
| Geometric mean       | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.3 ms: 1.21x faster                                      |
| python_startup_no_site | 6.96 ms                                                | 8.87 ms: 1.27x slower                                      |
| Geometric mean         | (ref)                                                  | 1.03x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 23.0 ms: 1.02x faster                                      |
| django_template | 35.2 ms                                                | 34.7 ms: 1.01x faster                                      |
| mako            | 11.1 ms                                                | 11.2 ms: 1.01x slower                                      |
| genshi_xml      | 50.9 ms                                                | 52.8 ms: 1.04x slower                                      |
| Geometric mean  | (ref)                                                  | 1.00x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles           | 2.41 ms                                                | 1.51 ms: 1.59x faster                                      |
| typing_runtime_protocols   | 165 us                                                 | 112 us: 1.47x faster                                       |
| gc_traversal               | 4.37 ms                                                | 3.55 ms: 1.23x faster                                      |
| python_startup             | 12.5 ms                                                | 10.3 ms: 1.21x faster                                      |
| mypy2                      | 1.04 sec                                               | 865 ms: 1.21x faster                                       |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.64 ms: 1.09x faster                                      |
| regex_v8                   | 26.2 ms                                                | 24.4 ms: 1.07x faster                                      |
| deepcopy_reduce            | 3.20 us                                                | 3.06 us: 1.05x faster                                      |
| crypto_pyaes               | 75.3 ms                                                | 72.0 ms: 1.05x faster                                      |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.04x faster                                       |
| mdp                        | 2.72 sec                                               | 2.61 sec: 1.04x faster                                     |
| logging_silent             | 102 ns                                                 | 97.7 ns: 1.04x faster                                      |
| json                       | 5.36 ms                                                | 5.19 ms: 1.03x faster                                      |
| deepcopy_memo              | 39.1 us                                                | 37.9 us: 1.03x faster                                      |
| go                         | 144 ms                                                 | 139 ms: 1.03x faster                                       |
| deepcopy                   | 358 us                                                 | 347 us: 1.03x faster                                       |
| pickle_pure_python         | 310 us                                                 | 302 us: 1.03x faster                                       |
| genshi_text                | 23.5 ms                                                | 23.0 ms: 1.02x faster                                      |
| xml_etree_process          | 60.6 ms                                                | 59.3 ms: 1.02x faster                                      |
| regex_effbot               | 3.73 ms                                                | 3.66 ms: 1.02x faster                                      |
| comprehensions             | 16.5 us                                                | 16.2 us: 1.02x faster                                      |
| telco                      | 8.54 ms                                                | 8.41 ms: 1.02x faster                                      |
| scimark_fft                | 364 ms                                                 | 359 ms: 1.01x faster                                       |
| richards_super             | 54.9 ms                                                | 54.1 ms: 1.01x faster                                      |
| django_template            | 35.2 ms                                                | 34.7 ms: 1.01x faster                                      |
| chameleon                  | 6.94 ms                                                | 6.85 ms: 1.01x faster                                      |
| richards                   | 48.7 ms                                                | 48.1 ms: 1.01x faster                                      |
| json_dumps                 | 10.6 ms                                                | 10.5 ms: 1.01x faster                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.26 ms: 1.01x faster                                      |
| raytrace                   | 267 ms                                                 | 265 ms: 1.01x faster                                       |
| bench_mp_pool              | 24.0 ms                                                | 23.8 ms: 1.01x faster                                      |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.01x faster                                       |
| regex_compile              | 132 ms                                                 | 132 ms: 1.00x faster                                       |
| scimark_monte_carlo        | 67.4 ms                                                | 67.2 ms: 1.00x faster                                      |
| unpickle_pure_python       | 216 us                                                 | 217 us: 1.00x slower                                       |
| sqlglot_normalize          | 108 ms                                                 | 108 ms: 1.00x slower                                       |
| deltablue                  | 3.23 ms                                                | 3.24 ms: 1.00x slower                                      |
| hexiom                     | 6.16 ms                                                | 6.20 ms: 1.01x slower                                      |
| pyflate                    | 471 ms                                                 | 474 ms: 1.01x slower                                       |
| pprint_safe_repr           | 728 ms                                                 | 734 ms: 1.01x slower                                       |
| sqlglot_optimize           | 53.7 ms                                                | 54.2 ms: 1.01x slower                                      |
| 2to3                       | 267 ms                                                 | 269 ms: 1.01x slower                                       |
| pprint_pformat             | 1.49 sec                                               | 1.51 sec: 1.01x slower                                     |
| mako                       | 11.1 ms                                                | 11.2 ms: 1.01x slower                                      |
| coroutines                 | 22.7 ms                                                | 23.0 ms: 1.01x slower                                      |
| pidigits                   | 186 ms                                                 | 189 ms: 1.02x slower                                       |
| logging_simple             | 5.72 us                                                | 5.83 us: 1.02x slower                                      |
| asyncio_websockets         | 552 ms                                                 | 563 ms: 1.02x slower                                       |
| bench_thread_pool          | 822 us                                                 | 838 us: 1.02x slower                                       |
| logging_format             | 6.40 us                                                | 6.53 us: 1.02x slower                                      |
| pycparser                  | 1.20 sec                                               | 1.23 sec: 1.02x slower                                     |
| docutils                   | 2.59 sec                                               | 2.65 sec: 1.02x slower                                     |
| regex_dna                  | 218 ms                                                 | 224 ms: 1.02x slower                                       |
| tomli_loads                | 2.14 sec                                               | 2.20 sec: 1.03x slower                                     |
| json_loads                 | 27.2 us                                                | 27.9 us: 1.03x slower                                      |
| xml_etree_parse            | 156 ms                                                 | 160 ms: 1.03x slower                                       |
| nqueens                    | 78.4 ms                                                | 81.0 ms: 1.03x slower                                      |
| genshi_xml                 | 50.9 ms                                                | 52.8 ms: 1.04x slower                                      |
| dulwich_log                | 64.3 ms                                                | 67.0 ms: 1.04x slower                                      |
| scimark_sor                | 124 ms                                                 | 129 ms: 1.04x slower                                       |
| generators                 | 29.0 ms                                                | 30.3 ms: 1.04x slower                                      |
| float                      | 79.2 ms                                                | 83.1 ms: 1.05x slower                                      |
| html5lib                   | 64.2 ms                                                | 67.4 ms: 1.05x slower                                      |
| tornado_http               | 92.4 ms                                                | 97.1 ms: 1.05x slower                                      |
| async_generators           | 436 ms                                                 | 459 ms: 1.05x slower                                       |
| chaos                      | 58.1 ms                                                | 61.2 ms: 1.05x slower                                      |
| xml_etree_iterparse        | 101 ms                                                 | 107 ms: 1.06x slower                                       |
| nbody                      | 87.0 ms                                                | 92.1 ms: 1.06x slower                                      |
| pathlib                    | 17.5 ms                                                | 18.7 ms: 1.07x slower                                      |
| coverage                   | 84.0 ms                                                | 96.3 ms: 1.15x slower                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 718 ms: 1.25x slower                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 585 ms: 1.26x slower                                       |
| async_tree_none            | 351 ms                                                 | 444 ms: 1.27x slower                                       |
| python_startup_no_site     | 6.96 ms                                                | 8.87 ms: 1.27x slower                                      |
| async_tree_memoization     | 442 ms                                                 | 571 ms: 1.29x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 733 ms: 1.34x slower                                       |
| async_tree_none_tg         | 321 ms                                                 | 455 ms: 1.42x slower                                       |
| async_tree_io              | 842 ms                                                 | 1.20 sec: 1.43x slower                                     |
| async_tree_io_tg           | 857 ms                                                 | 1.22 sec: 1.43x slower                                     |
| Geometric mean             | (ref)                                                  | 1.02x slower                                               |

Benchmark hidden because not significant (10): fannkuch, pylint, sympy_expand, sympy_str, thrift, sympy_integrate, scimark_lu, sympy_sum, sqlglot_transpile, xml_etree_generate
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (12) of results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.017x slower
# HPT report

- Reliability score: 99.85% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.88x