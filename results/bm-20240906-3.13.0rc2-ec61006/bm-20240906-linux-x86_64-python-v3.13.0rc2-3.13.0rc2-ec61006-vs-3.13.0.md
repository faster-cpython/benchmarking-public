# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc2
- machine: linux-x86_64
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.012x faster
- HPT reliability: 68.44%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 263 ms: 1.01x faster                                         |
| chameleon      | 6.94 ms                                                | 6.97 ms: 1.00x slower                                        |
| docutils       | 2.59 sec                                               | 2.74 sec: 1.06x slower                                       |
| html5lib       | 64.2 ms                                                | 64.9 ms: 1.01x slower                                        |
| tornado_http   | 92.4 ms                                                | 91.4 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 434 ms: 1.07x faster                                         |
| coroutines                 | 22.7 ms                                                | 22.1 ms: 1.03x faster                                        |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 564 ms: 1.03x slower                                         |
| async_tree_none            | 351 ms                                                 | 362 ms: 1.03x slower                                         |
| async_tree_none_tg         | 321 ms                                                 | 336 ms: 1.05x slower                                         |
| async_tree_io              | 842 ms                                                 | 889 ms: 1.06x slower                                         |
| async_tree_io_tg           | 857 ms                                                 | 931 ms: 1.09x slower                                         |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                 |

Benchmark hidden because not significant (3): async_generators, async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 79.2 ms                                                | 77.4 ms: 1.02x faster                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                         |
| nbody          | 87.0 ms                                                | 88.0 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                  | 1.00x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.2 ms: 1.09x faster                                        |
| regex_effbot   | 3.73 ms                                                | 3.49 ms: 1.07x faster                                        |
| regex_dna      | 218 ms                                                 | 216 ms: 1.01x faster                                         |
| regex_compile  | 132 ms                                                 | 133 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                  | 1.04x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 2.07 sec: 1.03x faster                                       |
| pickle_pure_python   | 310 us                                                 | 302 us: 1.03x faster                                         |
| json_dumps           | 10.6 ms                                                | 10.4 ms: 1.02x faster                                        |
| json_loads           | 27.2 us                                                | 27.1 us: 1.01x faster                                        |
| xml_etree_generate   | 86.7 ms                                                | 87.5 ms: 1.01x slower                                        |
| unpickle_pure_python | 216 us                                                 | 218 us: 1.01x slower                                         |
| xml_etree_iterparse  | 101 ms                                                 | 107 ms: 1.06x slower                                         |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                 |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.18x faster                                        |
| python_startup_no_site | 6.96 ms                                                | 6.96 ms: 1.00x faster                                        |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 35.2 ms                                                | 33.9 ms: 1.04x faster                                        |
| mako            | 11.1 ms                                                | 11.4 ms: 1.03x slower                                        |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                 |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mypy2                      | 1.04 sec                                               | 717 ms: 1.45x faster                                         |
| create_gc_cycles           | 2.41 ms                                                | 1.74 ms: 1.38x faster                                        |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.18x faster                                        |
| gc_traversal               | 4.37 ms                                                | 3.73 ms: 1.17x faster                                        |
| regex_v8                   | 26.2 ms                                                | 24.2 ms: 1.09x faster                                        |
| regex_effbot               | 3.73 ms                                                | 3.49 ms: 1.07x faster                                        |
| async_tree_memoization_tg  | 464 ms                                                 | 434 ms: 1.07x faster                                         |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                       |
| django_template            | 35.2 ms                                                | 33.9 ms: 1.04x faster                                        |
| tomli_loads                | 2.14 sec                                               | 2.07 sec: 1.03x faster                                       |
| richards_super             | 54.9 ms                                                | 53.2 ms: 1.03x faster                                        |
| richards                   | 48.7 ms                                                | 47.3 ms: 1.03x faster                                        |
| pickle_pure_python         | 310 us                                                 | 302 us: 1.03x faster                                         |
| coroutines                 | 22.7 ms                                                | 22.1 ms: 1.03x faster                                        |
| float                      | 79.2 ms                                                | 77.4 ms: 1.02x faster                                        |
| go                         | 144 ms                                                 | 141 ms: 1.02x faster                                         |
| json                       | 5.36 ms                                                | 5.24 ms: 1.02x faster                                        |
| pathlib                    | 17.5 ms                                                | 17.2 ms: 1.02x faster                                        |
| json_dumps                 | 10.6 ms                                                | 10.4 ms: 1.02x faster                                        |
| typing_runtime_protocols   | 165 us                                                 | 162 us: 1.02x faster                                         |
| fannkuch                   | 404 ms                                                 | 398 ms: 1.02x faster                                         |
| 2to3                       | 267 ms                                                 | 263 ms: 1.01x faster                                         |
| tornado_http               | 92.4 ms                                                | 91.4 ms: 1.01x faster                                        |
| dulwich_log                | 64.3 ms                                                | 63.7 ms: 1.01x faster                                        |
| regex_dna                  | 218 ms                                                 | 216 ms: 1.01x faster                                         |
| pyflate                    | 471 ms                                                 | 467 ms: 1.01x faster                                         |
| json_loads                 | 27.2 us                                                | 27.1 us: 1.01x faster                                        |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 5.01 ms: 1.01x faster                                        |
| bench_thread_pool          | 822 us                                                 | 818 us: 1.00x faster                                         |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                         |
| python_startup_no_site     | 6.96 ms                                                | 6.96 ms: 1.00x faster                                        |
| sqlglot_optimize           | 53.7 ms                                                | 53.9 ms: 1.00x slower                                        |
| generators                 | 29.0 ms                                                | 29.1 ms: 1.00x slower                                        |
| chameleon                  | 6.94 ms                                                | 6.97 ms: 1.00x slower                                        |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                         |
| deltablue                  | 3.23 ms                                                | 3.25 ms: 1.01x slower                                        |
| nqueens                    | 78.4 ms                                                | 78.9 ms: 1.01x slower                                        |
| deepcopy_reduce            | 3.20 us                                                | 3.22 us: 1.01x slower                                        |
| regex_compile              | 132 ms                                                 | 133 ms: 1.01x slower                                         |
| sqlglot_transpile          | 1.58 ms                                                | 1.60 ms: 1.01x slower                                        |
| xml_etree_generate         | 86.7 ms                                                | 87.5 ms: 1.01x slower                                        |
| deepcopy_memo              | 39.1 us                                                | 39.5 us: 1.01x slower                                        |
| sqlglot_normalize          | 108 ms                                                 | 109 ms: 1.01x slower                                         |
| telco                      | 8.54 ms                                                | 8.63 ms: 1.01x slower                                        |
| scimark_monte_carlo        | 67.4 ms                                                | 68.2 ms: 1.01x slower                                        |
| spectral_norm              | 115 ms                                                 | 117 ms: 1.01x slower                                         |
| html5lib                   | 64.2 ms                                                | 64.9 ms: 1.01x slower                                        |
| mdp                        | 2.72 sec                                               | 2.75 sec: 1.01x slower                                       |
| nbody                      | 87.0 ms                                                | 88.0 ms: 1.01x slower                                        |
| unpickle_pure_python       | 216 us                                                 | 218 us: 1.01x slower                                         |
| bpe_tokeniser              | 4.75 sec                                               | 4.80 sec: 1.01x slower                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.01x slower                                        |
| pprint_pformat             | 1.49 sec                                               | 1.52 sec: 1.02x slower                                       |
| scimark_sor                | 124 ms                                                 | 126 ms: 1.02x slower                                         |
| hexiom                     | 6.16 ms                                                | 6.29 ms: 1.02x slower                                        |
| pprint_safe_repr           | 728 ms                                                 | 744 ms: 1.02x slower                                         |
| chaos                      | 58.1 ms                                                | 59.6 ms: 1.03x slower                                        |
| mako                       | 11.1 ms                                                | 11.4 ms: 1.03x slower                                        |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 564 ms: 1.03x slower                                         |
| async_tree_none            | 351 ms                                                 | 362 ms: 1.03x slower                                         |
| async_tree_none_tg         | 321 ms                                                 | 336 ms: 1.05x slower                                         |
| async_tree_io              | 842 ms                                                 | 889 ms: 1.06x slower                                         |
| docutils                   | 2.59 sec                                               | 2.74 sec: 1.06x slower                                       |
| xml_etree_iterparse        | 101 ms                                                 | 107 ms: 1.06x slower                                         |
| async_tree_io_tg           | 857 ms                                                 | 931 ms: 1.09x slower                                         |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (25): genshi_text, thrift, logging_simple, comprehensions, genshi_xml, logging_format, async_generators, crypto_pyaes, sympy_str, raytrace, scimark_lu, meteor_contest, bench_mp_pool, deepcopy, sympy_integrate, coverage, sympy_expand, xml_etree_parse, scimark_fft, xml_etree_process, sympy_sum, logging_silent, async_tree_cpu_io_mixed, async_tree_memoization, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20240906-3.13.0rc2-ec61006/bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.012x faster
# HPT report

- Reliability score: 68.44% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.92x