# Results vs. 3.13.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: d343f97
- commit date: 2024-09-06
- overall geometric mean: 1.032x faster
- HPT reliability: 99.82%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 267 ms                                                 | 256 ms: 1.04x faster                                  |
| docutils       | 2.59 sec                                               | 2.66 sec: 1.02x slower                                |
| html5lib       | 64.2 ms                                                | 62.2 ms: 1.03x faster                                 |
| tornado_http   | 92.4 ms                                                | 91.6 ms: 1.01x faster                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 398 ms: 1.16x faster                                  |
| async_tree_memoization     | 442 ms                                                 | 387 ms: 1.14x faster                                  |
| async_tree_none            | 351 ms                                                 | 323 ms: 1.08x faster                                  |
| async_tree_none_tg         | 321 ms                                                 | 306 ms: 1.05x faster                                  |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 555 ms: 1.04x faster                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 536 ms: 1.02x faster                                  |
| async_generators           | 436 ms                                                 | 439 ms: 1.01x slower                                  |
| asyncio_websockets         | 552 ms                                                 | 558 ms: 1.01x slower                                  |
| coroutines                 | 22.7 ms                                                | 23.3 ms: 1.03x slower                                 |
| async_tree_io_tg           | 857 ms                                                 | 892 ms: 1.04x slower                                  |
| async_tree_io              | 842 ms                                                 | 927 ms: 1.10x slower                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| float          | 79.2 ms                                                | 77.8 ms: 1.02x faster                                 |
| nbody          | 87.0 ms                                                | 86.3 ms: 1.01x faster                                 |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.5 ms: 1.07x faster                                 |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                  |
| regex_effbot   | 3.73 ms                                                | 3.62 ms: 1.03x faster                                 |
| regex_dna      | 218 ms                                                 | 223 ms: 1.02x slower                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| xml_etree_process    | 60.6 ms                                                | 58.6 ms: 1.04x faster                                 |
| pickle_pure_python   | 310 us                                                 | 300 us: 1.03x faster                                  |
| tomli_loads          | 2.14 sec                                               | 2.08 sec: 1.03x faster                                |
| xml_etree_generate   | 86.7 ms                                                | 85.2 ms: 1.02x faster                                 |
| unpickle_pure_python | 216 us                                                 | 214 us: 1.01x faster                                  |
| json_dumps           | 10.6 ms                                                | 10.5 ms: 1.01x faster                                 |
| json_loads           | 27.2 us                                                | 28.4 us: 1.04x slower                                 |
| xml_etree_iterparse  | 101 ms                                                 | 106 ms: 1.05x slower                                  |
| Geometric mean       | (ref)                                                  | 1.00x faster                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.18x faster                                 |
| python_startup_no_site | 6.96 ms                                                | 7.05 ms: 1.01x slower                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 22.1 ms: 1.06x faster                                 |
| genshi_xml      | 50.9 ms                                                | 48.7 ms: 1.05x faster                                 |
| django_template | 35.2 ms                                                | 34.2 ms: 1.03x faster                                 |
| Geometric mean  | (ref)                                                  | 1.03x faster                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| create_gc_cycles           | 2.41 ms                                                | 1.72 ms: 1.40x faster                                 |
| deepcopy                   | 358 us                                                 | 258 us: 1.39x faster                                  |
| deepcopy_memo              | 39.1 us                                                | 29.7 us: 1.32x faster                                 |
| gc_traversal               | 4.37 ms                                                | 3.56 ms: 1.23x faster                                 |
| go                         | 144 ms                                                 | 118 ms: 1.22x faster                                  |
| deepcopy_reduce            | 3.20 us                                                | 2.69 us: 1.19x faster                                 |
| python_startup             | 12.5 ms                                                | 10.6 ms: 1.18x faster                                 |
| async_tree_memoization_tg  | 464 ms                                                 | 398 ms: 1.16x faster                                  |
| async_tree_memoization     | 442 ms                                                 | 387 ms: 1.14x faster                                  |
| pathlib                    | 17.5 ms                                                | 15.9 ms: 1.10x faster                                 |
| async_tree_none            | 351 ms                                                 | 323 ms: 1.08x faster                                  |
| regex_v8                   | 26.2 ms                                                | 24.5 ms: 1.07x faster                                 |
| genshi_text                | 23.5 ms                                                | 22.1 ms: 1.06x faster                                 |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.05x faster                                |
| thrift                     | 809 us                                                 | 772 us: 1.05x faster                                  |
| richards                   | 48.7 ms                                                | 46.5 ms: 1.05x faster                                 |
| async_tree_none_tg         | 321 ms                                                 | 306 ms: 1.05x faster                                  |
| genshi_xml                 | 50.9 ms                                                | 48.7 ms: 1.05x faster                                 |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.83 ms: 1.04x faster                                 |
| richards_super             | 54.9 ms                                                | 52.5 ms: 1.04x faster                                 |
| 2to3                       | 267 ms                                                 | 256 ms: 1.04x faster                                  |
| generators                 | 29.0 ms                                                | 27.8 ms: 1.04x faster                                 |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 555 ms: 1.04x faster                                  |
| bench_thread_pool          | 822 us                                                 | 790 us: 1.04x faster                                  |
| xml_etree_process          | 60.6 ms                                                | 58.6 ms: 1.04x faster                                 |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                  |
| typing_runtime_protocols   | 165 us                                                 | 159 us: 1.03x faster                                  |
| pickle_pure_python         | 310 us                                                 | 300 us: 1.03x faster                                  |
| telco                      | 8.54 ms                                                | 8.27 ms: 1.03x faster                                 |
| html5lib                   | 64.2 ms                                                | 62.2 ms: 1.03x faster                                 |
| crypto_pyaes               | 75.3 ms                                                | 73.1 ms: 1.03x faster                                 |
| regex_effbot               | 3.73 ms                                                | 3.62 ms: 1.03x faster                                 |
| tomli_loads                | 2.14 sec                                               | 2.08 sec: 1.03x faster                                |
| django_template            | 35.2 ms                                                | 34.2 ms: 1.03x faster                                 |
| raytrace                   | 267 ms                                                 | 260 ms: 1.03x faster                                  |
| sympy_str                  | 275 ms                                                 | 268 ms: 1.02x faster                                  |
| logging_format             | 6.40 us                                                | 6.26 us: 1.02x faster                                 |
| pprint_safe_repr           | 728 ms                                                 | 713 ms: 1.02x faster                                  |
| xml_etree_generate         | 86.7 ms                                                | 85.2 ms: 1.02x faster                                 |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 536 ms: 1.02x faster                                  |
| float                      | 79.2 ms                                                | 77.8 ms: 1.02x faster                                 |
| sympy_integrate            | 19.9 ms                                                | 19.6 ms: 1.02x faster                                 |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.01x faster                                  |
| sympy_expand               | 463 ms                                                 | 457 ms: 1.01x faster                                  |
| pprint_pformat             | 1.49 sec                                               | 1.47 sec: 1.01x faster                                |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.01x faster                                  |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                  |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                  |
| sqlglot_optimize           | 53.7 ms                                                | 53.3 ms: 1.01x faster                                 |
| tornado_http               | 92.4 ms                                                | 91.6 ms: 1.01x faster                                 |
| unpickle_pure_python       | 216 us                                                 | 214 us: 1.01x faster                                  |
| nbody                      | 87.0 ms                                                | 86.3 ms: 1.01x faster                                 |
| json_dumps                 | 10.6 ms                                                | 10.5 ms: 1.01x faster                                 |
| scimark_lu                 | 113 ms                                                 | 112 ms: 1.01x faster                                  |
| deltablue                  | 3.23 ms                                                | 3.21 ms: 1.01x faster                                 |
| hexiom                     | 6.16 ms                                                | 6.14 ms: 1.00x faster                                 |
| scimark_fft                | 364 ms                                                 | 363 ms: 1.00x faster                                  |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                  |
| mdp                        | 2.72 sec                                               | 2.73 sec: 1.00x slower                                |
| dulwich_log                | 64.3 ms                                                | 64.6 ms: 1.00x slower                                 |
| async_generators           | 436 ms                                                 | 439 ms: 1.01x slower                                  |
| chaos                      | 58.1 ms                                                | 58.5 ms: 1.01x slower                                 |
| pyflate                    | 471 ms                                                 | 475 ms: 1.01x slower                                  |
| logging_simple             | 5.72 us                                                | 5.77 us: 1.01x slower                                 |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.01x slower                                 |
| logging_silent             | 102 ns                                                 | 103 ns: 1.01x slower                                  |
| asyncio_websockets         | 552 ms                                                 | 558 ms: 1.01x slower                                  |
| python_startup_no_site     | 6.96 ms                                                | 7.05 ms: 1.01x slower                                 |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                 |
| fannkuch                   | 404 ms                                                 | 410 ms: 1.01x slower                                  |
| scimark_sor                | 124 ms                                                 | 126 ms: 1.02x slower                                  |
| regex_dna                  | 218 ms                                                 | 223 ms: 1.02x slower                                  |
| bpe_tokeniser              | 4.75 sec                                               | 4.84 sec: 1.02x slower                                |
| docutils                   | 2.59 sec                                               | 2.66 sec: 1.02x slower                                |
| coroutines                 | 22.7 ms                                                | 23.3 ms: 1.03x slower                                 |
| coverage                   | 84.0 ms                                                | 86.6 ms: 1.03x slower                                 |
| nqueens                    | 78.4 ms                                                | 81.2 ms: 1.04x slower                                 |
| async_tree_io_tg           | 857 ms                                                 | 892 ms: 1.04x slower                                  |
| json_loads                 | 27.2 us                                                | 28.4 us: 1.04x slower                                 |
| xml_etree_iterparse        | 101 ms                                                 | 106 ms: 1.05x slower                                  |
| async_tree_io              | 842 ms                                                 | 927 ms: 1.10x slower                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                          |

Benchmark hidden because not significant (7): scimark_monte_carlo, json, mako, bench_mp_pool, sqlglot_transpile, xml_etree_parse, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240906-3.14.0a0-d343f97/bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.032x faster
# HPT report

- Reliability score: 99.82% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x