# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a2
- machine: linux-x86_64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.036x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 0.86x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 272 ms: 1.02x slower                                       |
| docutils       | 2.59 sec                                               | 2.69 sec: 1.04x slower                                     |
| html5lib       | 64.2 ms                                                | 66.3 ms: 1.03x slower                                      |
| tornado_http   | 92.4 ms                                                | 97.6 ms: 1.06x slower                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| coroutines                 | 22.7 ms                                                | 21.8 ms: 1.04x faster                                      |
| asyncio_websockets         | 552 ms                                                 | 563 ms: 1.02x slower                                       |
| async_generators           | 436 ms                                                 | 459 ms: 1.05x slower                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 733 ms: 1.27x slower                                       |
| async_tree_none            | 351 ms                                                 | 451 ms: 1.29x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 583 ms: 1.32x slower                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 618 ms: 1.33x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 760 ms: 1.39x slower                                       |
| async_tree_io              | 842 ms                                                 | 1.22 sec: 1.45x slower                                     |
| async_tree_none_tg         | 321 ms                                                 | 471 ms: 1.47x slower                                       |
| async_tree_io_tg           | 857 ms                                                 | 1.26 sec: 1.47x slower                                     |
| Geometric mean             | (ref)                                                  | 1.26x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 91.0 ms: 1.05x slower                                      |
| float          | 79.2 ms                                                | 83.5 ms: 1.05x slower                                      |
| pidigits       | 186 ms                                                 | 197 ms: 1.06x slower                                       |
| Geometric mean | (ref)                                                  | 1.05x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.0 ms: 1.05x faster                                      |
| regex_effbot   | 3.73 ms                                                | 3.57 ms: 1.05x faster                                      |
| regex_compile  | 132 ms                                                 | 137 ms: 1.04x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 310 us                                                 | 313 us: 1.01x slower                                       |
| json_dumps           | 10.6 ms                                                | 10.7 ms: 1.01x slower                                      |
| xml_etree_generate   | 86.7 ms                                                | 88.2 ms: 1.02x slower                                      |
| unpickle_pure_python | 216 us                                                 | 224 us: 1.04x slower                                       |
| tomli_loads          | 2.14 sec                                               | 2.23 sec: 1.04x slower                                     |
| xml_etree_parse      | 156 ms                                                 | 162 ms: 1.04x slower                                       |
| json_loads           | 27.2 us                                                | 28.7 us: 1.05x slower                                      |
| xml_etree_iterparse  | 101 ms                                                 | 108 ms: 1.07x slower                                       |
| Geometric mean       | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.7 ms: 1.17x faster                                      |
| python_startup_no_site | 6.96 ms                                                | 9.26 ms: 1.33x slower                                      |
| Geometric mean         | (ref)                                                  | 1.07x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text    | 23.5 ms                                                | 23.8 ms: 1.01x slower                                      |
| genshi_xml     | 50.9 ms                                                | 52.1 ms: 1.02x slower                                      |
| mako           | 11.1 ms                                                | 11.7 ms: 1.05x slower                                      |
| Geometric mean | (ref)                                                  | 1.02x slower                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles           | 2.41 ms                                                | 1.48 ms: 1.62x faster                                      |
| typing_runtime_protocols   | 165 us                                                 | 119 us: 1.38x faster                                       |
| mypy2                      | 1.04 sec                                               | 866 ms: 1.20x faster                                       |
| python_startup             | 12.5 ms                                                | 10.7 ms: 1.17x faster                                      |
| regex_v8                   | 26.2 ms                                                | 25.0 ms: 1.05x faster                                      |
| regex_effbot               | 3.73 ms                                                | 3.57 ms: 1.05x faster                                      |
| coroutines                 | 22.7 ms                                                | 21.8 ms: 1.04x faster                                      |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.04x faster                                       |
| mdp                        | 2.72 sec                                               | 2.64 sec: 1.03x faster                                     |
| crypto_pyaes               | 75.3 ms                                                | 73.3 ms: 1.03x faster                                      |
| json                       | 5.36 ms                                                | 5.24 ms: 1.02x faster                                      |
| deepcopy_reduce            | 3.20 us                                                | 3.14 us: 1.02x faster                                      |
| deepcopy                   | 358 us                                                 | 354 us: 1.01x faster                                       |
| pycparser                  | 1.20 sec                                               | 1.19 sec: 1.01x faster                                     |
| sympy_expand               | 463 ms                                                 | 459 ms: 1.01x faster                                       |
| sympy_str                  | 275 ms                                                 | 273 ms: 1.01x faster                                       |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.00x faster                                       |
| sympy_integrate            | 19.9 ms                                                | 20.0 ms: 1.00x slower                                      |
| sympy_sum                  | 150 ms                                                 | 151 ms: 1.01x slower                                       |
| pickle_pure_python         | 310 us                                                 | 313 us: 1.01x slower                                       |
| json_dumps                 | 10.6 ms                                                | 10.7 ms: 1.01x slower                                      |
| sqlglot_optimize           | 53.7 ms                                                | 54.3 ms: 1.01x slower                                      |
| genshi_text                | 23.5 ms                                                | 23.8 ms: 1.01x slower                                      |
| meteor_contest             | 109 ms                                                 | 110 ms: 1.01x slower                                       |
| logging_format             | 6.40 us                                                | 6.50 us: 1.02x slower                                      |
| xml_etree_generate         | 86.7 ms                                                | 88.2 ms: 1.02x slower                                      |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 5.13 ms: 1.02x slower                                      |
| deepcopy_memo              | 39.1 us                                                | 39.8 us: 1.02x slower                                      |
| 2to3                       | 267 ms                                                 | 272 ms: 1.02x slower                                       |
| asyncio_websockets         | 552 ms                                                 | 563 ms: 1.02x slower                                       |
| richards                   | 48.7 ms                                                | 49.7 ms: 1.02x slower                                      |
| scimark_sor                | 124 ms                                                 | 126 ms: 1.02x slower                                       |
| genshi_xml                 | 50.9 ms                                                | 52.1 ms: 1.02x slower                                      |
| hexiom                     | 6.16 ms                                                | 6.32 ms: 1.02x slower                                      |
| go                         | 144 ms                                                 | 148 ms: 1.03x slower                                       |
| pprint_pformat             | 1.49 sec                                               | 1.54 sec: 1.03x slower                                     |
| pyflate                    | 471 ms                                                 | 484 ms: 1.03x slower                                       |
| scimark_fft                | 364 ms                                                 | 375 ms: 1.03x slower                                       |
| logging_simple             | 5.72 us                                                | 5.89 us: 1.03x slower                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.31 ms: 1.03x slower                                      |
| sqlglot_transpile          | 1.58 ms                                                | 1.64 ms: 1.03x slower                                      |
| html5lib                   | 64.2 ms                                                | 66.3 ms: 1.03x slower                                      |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                      |
| scimark_lu                 | 113 ms                                                 | 117 ms: 1.03x slower                                       |
| pprint_safe_repr           | 728 ms                                                 | 753 ms: 1.03x slower                                       |
| docutils                   | 2.59 sec                                               | 2.69 sec: 1.04x slower                                     |
| regex_compile              | 132 ms                                                 | 137 ms: 1.04x slower                                       |
| bench_thread_pool          | 822 us                                                 | 852 us: 1.04x slower                                       |
| scimark_monte_carlo        | 67.4 ms                                                | 70.0 ms: 1.04x slower                                      |
| unpickle_pure_python       | 216 us                                                 | 224 us: 1.04x slower                                       |
| tomli_loads                | 2.14 sec                                               | 2.23 sec: 1.04x slower                                     |
| generators                 | 29.0 ms                                                | 30.1 ms: 1.04x slower                                      |
| xml_etree_parse            | 156 ms                                                 | 162 ms: 1.04x slower                                       |
| nbody                      | 87.0 ms                                                | 91.0 ms: 1.05x slower                                      |
| dulwich_log                | 64.3 ms                                                | 67.6 ms: 1.05x slower                                      |
| mako                       | 11.1 ms                                                | 11.7 ms: 1.05x slower                                      |
| async_generators           | 436 ms                                                 | 459 ms: 1.05x slower                                       |
| json_loads                 | 27.2 us                                                | 28.7 us: 1.05x slower                                      |
| float                      | 79.2 ms                                                | 83.5 ms: 1.05x slower                                      |
| tornado_http               | 92.4 ms                                                | 97.6 ms: 1.06x slower                                      |
| pidigits                   | 186 ms                                                 | 197 ms: 1.06x slower                                       |
| pathlib                    | 17.5 ms                                                | 18.6 ms: 1.06x slower                                      |
| raytrace                   | 267 ms                                                 | 284 ms: 1.07x slower                                       |
| nqueens                    | 78.4 ms                                                | 83.5 ms: 1.07x slower                                      |
| deltablue                  | 3.23 ms                                                | 3.44 ms: 1.07x slower                                      |
| xml_etree_iterparse        | 101 ms                                                 | 108 ms: 1.07x slower                                       |
| logging_silent             | 102 ns                                                 | 109 ns: 1.07x slower                                       |
| chaos                      | 58.1 ms                                                | 63.4 ms: 1.09x slower                                      |
| coverage                   | 84.0 ms                                                | 95.2 ms: 1.13x slower                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 733 ms: 1.27x slower                                       |
| async_tree_none            | 351 ms                                                 | 451 ms: 1.29x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 583 ms: 1.32x slower                                       |
| python_startup_no_site     | 6.96 ms                                                | 9.26 ms: 1.33x slower                                      |
| async_tree_memoization_tg  | 464 ms                                                 | 618 ms: 1.33x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 760 ms: 1.39x slower                                       |
| async_tree_io              | 842 ms                                                 | 1.22 sec: 1.45x slower                                     |
| async_tree_none_tg         | 321 ms                                                 | 471 ms: 1.47x slower                                       |
| async_tree_io_tg           | 857 ms                                                 | 1.26 sec: 1.47x slower                                     |
| Geometric mean             | (ref)                                                  | 1.04x slower                                               |

Benchmark hidden because not significant (11): fannkuch, thrift, xml_etree_process, bench_mp_pool, telco, chameleon, gc_traversal, pylint, django_template, richards_super, regex_dna
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (12) of results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.036x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 0.86x