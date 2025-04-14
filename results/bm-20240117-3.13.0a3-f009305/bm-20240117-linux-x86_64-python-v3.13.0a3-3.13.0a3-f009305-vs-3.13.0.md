# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a3
- machine: linux-x86_64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.021x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.87x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 270 ms: 1.01x slower                                       |
| chameleon      | 6.94 ms                                                | 6.87 ms: 1.01x faster                                      |
| docutils       | 2.59 sec                                               | 2.68 sec: 1.03x slower                                     |
| html5lib       | 64.2 ms                                                | 67.9 ms: 1.06x slower                                      |
| tornado_http   | 92.4 ms                                                | 96.8 ms: 1.05x slower                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| coroutines                 | 22.7 ms                                                | 22.3 ms: 1.02x faster                                      |
| asyncio_websockets         | 552 ms                                                 | 563 ms: 1.02x slower                                       |
| async_generators           | 436 ms                                                 | 454 ms: 1.04x slower                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 724 ms: 1.26x slower                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 586 ms: 1.26x slower                                       |
| async_tree_none            | 351 ms                                                 | 446 ms: 1.27x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 574 ms: 1.30x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 734 ms: 1.34x slower                                       |
| async_tree_none_tg         | 321 ms                                                 | 447 ms: 1.40x slower                                       |
| async_tree_io_tg           | 857 ms                                                 | 1.21 sec: 1.42x slower                                     |
| async_tree_io              | 842 ms                                                 | 1.21 sec: 1.44x slower                                     |
| Geometric mean             | (ref)                                                  | 1.24x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 191 ms: 1.02x slower                                       |
| nbody          | 87.0 ms                                                | 89.5 ms: 1.03x slower                                      |
| float          | 79.2 ms                                                | 82.0 ms: 1.04x slower                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.4 ms: 1.03x faster                                      |
| regex_effbot   | 3.73 ms                                                | 3.68 ms: 1.01x faster                                      |
| regex_compile  | 132 ms                                                 | 131 ms: 1.01x faster                                       |
| regex_dna      | 218 ms                                                 | 230 ms: 1.05x slower                                       |
| Geometric mean | (ref)                                                  | 1.00x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 310 us                                                 | 302 us: 1.03x faster                                       |
| xml_etree_process    | 60.6 ms                                                | 59.9 ms: 1.01x faster                                      |
| json_dumps           | 10.6 ms                                                | 10.5 ms: 1.01x faster                                      |
| xml_etree_generate   | 86.7 ms                                                | 87.4 ms: 1.01x slower                                      |
| tomli_loads          | 2.14 sec                                               | 2.16 sec: 1.01x slower                                     |
| unpickle_pure_python | 216 us                                                 | 218 us: 1.01x slower                                       |
| xml_etree_parse      | 156 ms                                                 | 161 ms: 1.03x slower                                       |
| xml_etree_iterparse  | 101 ms                                                 | 106 ms: 1.05x slower                                       |
| json_loads           | 27.2 us                                                | 28.7 us: 1.06x slower                                      |
| Geometric mean       | (ref)                                                  | 1.01x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.4 ms: 1.20x faster                                      |
| python_startup_no_site | 6.96 ms                                                | 8.92 ms: 1.28x slower                                      |
| Geometric mean         | (ref)                                                  | 1.03x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 23.2 ms: 1.01x faster                                      |
| django_template | 35.2 ms                                                | 34.7 ms: 1.01x faster                                      |
| mako            | 11.1 ms                                                | 11.3 ms: 1.02x slower                                      |
| genshi_xml      | 50.9 ms                                                | 52.1 ms: 1.02x slower                                      |
| Geometric mean  | (ref)                                                  | 1.00x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles           | 2.41 ms                                                | 1.51 ms: 1.59x faster                                      |
| typing_runtime_protocols   | 165 us                                                 | 110 us: 1.50x faster                                       |
| mypy2                      | 1.04 sec                                               | 865 ms: 1.21x faster                                       |
| python_startup             | 12.5 ms                                                | 10.4 ms: 1.20x faster                                      |
| gc_traversal               | 4.37 ms                                                | 3.78 ms: 1.15x faster                                      |
| mdp                        | 2.72 sec                                               | 2.58 sec: 1.05x faster                                     |
| crypto_pyaes               | 75.3 ms                                                | 72.3 ms: 1.04x faster                                      |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.04x faster                                       |
| regex_v8                   | 26.2 ms                                                | 25.4 ms: 1.03x faster                                      |
| deepcopy_reduce            | 3.20 us                                                | 3.11 us: 1.03x faster                                      |
| go                         | 144 ms                                                 | 140 ms: 1.03x faster                                       |
| pickle_pure_python         | 310 us                                                 | 302 us: 1.03x faster                                       |
| deepcopy                   | 358 us                                                 | 350 us: 1.02x faster                                       |
| deepcopy_memo              | 39.1 us                                                | 38.4 us: 1.02x faster                                      |
| coroutines                 | 22.7 ms                                                | 22.3 ms: 1.02x faster                                      |
| thrift                     | 809 us                                                 | 796 us: 1.02x faster                                       |
| genshi_text                | 23.5 ms                                                | 23.2 ms: 1.01x faster                                      |
| comprehensions             | 16.5 us                                                | 16.3 us: 1.01x faster                                      |
| regex_effbot               | 3.73 ms                                                | 3.68 ms: 1.01x faster                                      |
| django_template            | 35.2 ms                                                | 34.7 ms: 1.01x faster                                      |
| xml_etree_process          | 60.6 ms                                                | 59.9 ms: 1.01x faster                                      |
| raytrace                   | 267 ms                                                 | 264 ms: 1.01x faster                                       |
| hexiom                     | 6.16 ms                                                | 6.10 ms: 1.01x faster                                      |
| chameleon                  | 6.94 ms                                                | 6.87 ms: 1.01x faster                                      |
| json_dumps                 | 10.6 ms                                                | 10.5 ms: 1.01x faster                                      |
| regex_compile              | 132 ms                                                 | 131 ms: 1.01x faster                                       |
| pycparser                  | 1.20 sec                                               | 1.19 sec: 1.01x faster                                     |
| bench_mp_pool              | 24.0 ms                                                | 23.8 ms: 1.01x faster                                      |
| sympy_integrate            | 19.9 ms                                                | 20.0 ms: 1.00x slower                                      |
| scimark_fft                | 364 ms                                                 | 366 ms: 1.00x slower                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.00x slower                                      |
| richards                   | 48.7 ms                                                | 48.9 ms: 1.00x slower                                      |
| generators                 | 29.0 ms                                                | 29.2 ms: 1.01x slower                                      |
| meteor_contest             | 109 ms                                                 | 110 ms: 1.01x slower                                       |
| xml_etree_generate         | 86.7 ms                                                | 87.4 ms: 1.01x slower                                      |
| tomli_loads                | 2.14 sec                                               | 2.16 sec: 1.01x slower                                     |
| sympy_sum                  | 150 ms                                                 | 152 ms: 1.01x slower                                       |
| scimark_lu                 | 113 ms                                                 | 114 ms: 1.01x slower                                       |
| unpickle_pure_python       | 216 us                                                 | 218 us: 1.01x slower                                       |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 5.10 ms: 1.01x slower                                      |
| 2to3                       | 267 ms                                                 | 270 ms: 1.01x slower                                       |
| sqlglot_transpile          | 1.58 ms                                                | 1.61 ms: 1.01x slower                                      |
| sqlglot_normalize          | 108 ms                                                 | 109 ms: 1.02x slower                                       |
| scimark_monte_carlo        | 67.4 ms                                                | 68.6 ms: 1.02x slower                                      |
| mako                       | 11.1 ms                                                | 11.3 ms: 1.02x slower                                      |
| sqlglot_optimize           | 53.7 ms                                                | 54.8 ms: 1.02x slower                                      |
| asyncio_websockets         | 552 ms                                                 | 563 ms: 1.02x slower                                       |
| logging_format             | 6.40 us                                                | 6.53 us: 1.02x slower                                      |
| genshi_xml                 | 50.9 ms                                                | 52.1 ms: 1.02x slower                                      |
| pidigits                   | 186 ms                                                 | 191 ms: 1.02x slower                                       |
| pprint_safe_repr           | 728 ms                                                 | 745 ms: 1.02x slower                                       |
| bench_thread_pool          | 822 us                                                 | 842 us: 1.02x slower                                       |
| pprint_pformat             | 1.49 sec                                               | 1.53 sec: 1.03x slower                                     |
| nbody                      | 87.0 ms                                                | 89.5 ms: 1.03x slower                                      |
| logging_simple             | 5.72 us                                                | 5.89 us: 1.03x slower                                      |
| nqueens                    | 78.4 ms                                                | 80.7 ms: 1.03x slower                                      |
| chaos                      | 58.1 ms                                                | 59.9 ms: 1.03x slower                                      |
| docutils                   | 2.59 sec                                               | 2.68 sec: 1.03x slower                                     |
| logging_silent             | 102 ns                                                 | 105 ns: 1.03x slower                                       |
| xml_etree_parse            | 156 ms                                                 | 161 ms: 1.03x slower                                       |
| float                      | 79.2 ms                                                | 82.0 ms: 1.04x slower                                      |
| dulwich_log                | 64.3 ms                                                | 66.8 ms: 1.04x slower                                      |
| async_generators           | 436 ms                                                 | 454 ms: 1.04x slower                                       |
| tornado_http               | 92.4 ms                                                | 96.8 ms: 1.05x slower                                      |
| xml_etree_iterparse        | 101 ms                                                 | 106 ms: 1.05x slower                                       |
| regex_dna                  | 218 ms                                                 | 230 ms: 1.05x slower                                       |
| pathlib                    | 17.5 ms                                                | 18.5 ms: 1.05x slower                                      |
| json_loads                 | 27.2 us                                                | 28.7 us: 1.06x slower                                      |
| html5lib                   | 64.2 ms                                                | 67.9 ms: 1.06x slower                                      |
| scimark_sor                | 124 ms                                                 | 131 ms: 1.06x slower                                       |
| coverage                   | 84.0 ms                                                | 95.8 ms: 1.14x slower                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 724 ms: 1.26x slower                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 586 ms: 1.26x slower                                       |
| async_tree_none            | 351 ms                                                 | 446 ms: 1.27x slower                                       |
| python_startup_no_site     | 6.96 ms                                                | 8.92 ms: 1.28x slower                                      |
| async_tree_memoization     | 442 ms                                                 | 574 ms: 1.30x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 734 ms: 1.34x slower                                       |
| async_tree_none_tg         | 321 ms                                                 | 447 ms: 1.40x slower                                       |
| async_tree_io_tg           | 857 ms                                                 | 1.21 sec: 1.42x slower                                     |
| async_tree_io              | 842 ms                                                 | 1.21 sec: 1.44x slower                                     |
| Geometric mean             | (ref)                                                  | 1.02x slower                                               |

Benchmark hidden because not significant (9): fannkuch, sympy_str, pyflate, telco, deltablue, pylint, richards_super, sympy_expand, json
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (12) of results/bm-20240117-3.13.0a3-f009305/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.021x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.87x