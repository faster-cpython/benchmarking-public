# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a2
- machine: linux-x86_64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.221x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x slower
- Memory change: 0.53x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 294 ms: 1.10x slower                                       |
| chameleon      | 6.94 ms                                                | 7.76 ms: 1.12x slower                                      |
| docutils       | 2.59 sec                                               | 2.89 sec: 1.11x slower                                     |
| html5lib       | 64.2 ms                                                | 71.7 ms: 1.12x slower                                      |
| tornado_http   | 92.4 ms                                                | 108 ms: 1.16x slower                                       |
| Geometric mean | (ref)                                                  | 1.12x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| asyncio_websockets         | 552 ms                                                 | 564 ms: 1.02x slower                                       |
| coroutines                 | 22.7 ms                                                | 24.8 ms: 1.09x slower                                      |
| async_generators           | 436 ms                                                 | 500 ms: 1.15x slower                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 804 ms: 1.39x slower                                       |
| async_tree_none            | 351 ms                                                 | 509 ms: 1.45x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 657 ms: 1.49x slower                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 692 ms: 1.49x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 850 ms: 1.56x slower                                       |
| async_tree_io              | 842 ms                                                 | 1.39 sec: 1.65x slower                                     |
| async_tree_none_tg         | 321 ms                                                 | 540 ms: 1.68x slower                                       |
| async_tree_io_tg           | 857 ms                                                 | 1.45 sec: 1.70x slower                                     |
| Geometric mean             | (ref)                                                  | 1.41x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 194 ms: 1.04x slower                                       |
| float          | 79.2 ms                                                | 95.5 ms: 1.21x slower                                      |
| nbody          | 87.0 ms                                                | 110 ms: 1.26x slower                                       |
| Geometric mean | (ref)                                                  | 1.16x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.9 ms: 1.01x faster                                      |
| regex_dna      | 218 ms                                                 | 222 ms: 1.02x slower                                       |
| regex_effbot   | 3.73 ms                                                | 3.83 ms: 1.03x slower                                      |
| regex_compile  | 132 ms                                                 | 149 ms: 1.13x slower                                       |
| Geometric mean | (ref)                                                  | 1.04x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 10.6 ms                                                | 11.3 ms: 1.07x slower                                      |
| pickle_pure_python   | 310 us                                                 | 335 us: 1.08x slower                                       |
| tomli_loads          | 2.14 sec                                               | 2.37 sec: 1.10x slower                                     |
| xml_etree_iterparse  | 101 ms                                                 | 114 ms: 1.13x slower                                       |
| json_loads           | 27.2 us                                                | 30.9 us: 1.14x slower                                      |
| unpickle_pure_python | 216 us                                                 | 246 us: 1.14x slower                                       |
| xml_etree_parse      | 156 ms                                                 | 472 ms: 3.03x slower                                       |
| xml_etree_process    | 60.6 ms                                                | 1.03 sec: 16.96x slower                                    |
| xml_etree_generate   | 86.7 ms                                                | 1.58 sec: 18.23x slower                                    |
| Geometric mean       | (ref)                                                  | 2.29x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 11.1 ms: 1.12x faster                                      |
| python_startup_no_site | 6.96 ms                                                | 9.60 ms: 1.38x slower                                      |
| Geometric mean         | (ref)                                                  | 1.11x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 24.9 ms: 1.06x slower                                      |
| django_template | 35.2 ms                                                | 38.3 ms: 1.09x slower                                      |
| genshi_xml      | 50.9 ms                                                | 56.2 ms: 1.10x slower                                      |
| mako            | 11.1 ms                                                | 12.9 ms: 1.17x slower                                      |
| Geometric mean  | (ref)                                                  | 1.10x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles           | 2.41 ms                                                | 1.22 ms: 1.98x faster                                      |
| typing_runtime_protocols   | 165 us                                                 | 127 us: 1.29x faster                                       |
| gc_traversal               | 4.37 ms                                                | 3.64 ms: 1.20x faster                                      |
| python_startup             | 12.5 ms                                                | 11.1 ms: 1.12x faster                                      |
| bench_mp_pool              | 24.0 ms                                                | 22.6 ms: 1.06x faster                                      |
| regex_v8                   | 26.2 ms                                                | 25.9 ms: 1.01x faster                                      |
| regex_dna                  | 218 ms                                                 | 222 ms: 1.02x slower                                       |
| asyncio_websockets         | 552 ms                                                 | 564 ms: 1.02x slower                                       |
| regex_effbot               | 3.73 ms                                                | 3.83 ms: 1.03x slower                                      |
| pidigits                   | 186 ms                                                 | 194 ms: 1.04x slower                                       |
| genshi_text                | 23.5 ms                                                | 24.9 ms: 1.06x slower                                      |
| json                       | 5.36 ms                                                | 5.68 ms: 1.06x slower                                      |
| pycparser                  | 1.20 sec                                               | 1.27 sec: 1.06x slower                                     |
| mdp                        | 2.72 sec                                               | 2.89 sec: 1.06x slower                                     |
| crypto_pyaes               | 75.3 ms                                                | 80.1 ms: 1.06x slower                                      |
| richards                   | 48.7 ms                                                | 51.9 ms: 1.07x slower                                      |
| json_dumps                 | 10.6 ms                                                | 11.3 ms: 1.07x slower                                      |
| meteor_contest             | 109 ms                                                 | 117 ms: 1.07x slower                                       |
| richards_super             | 54.9 ms                                                | 59.1 ms: 1.08x slower                                      |
| generators                 | 29.0 ms                                                | 31.2 ms: 1.08x slower                                      |
| pickle_pure_python         | 310 us                                                 | 335 us: 1.08x slower                                       |
| pyflate                    | 471 ms                                                 | 510 ms: 1.08x slower                                       |
| django_template            | 35.2 ms                                                | 38.3 ms: 1.09x slower                                      |
| go                         | 144 ms                                                 | 157 ms: 1.09x slower                                       |
| pylint                     | 313 ms                                                 | 341 ms: 1.09x slower                                       |
| coroutines                 | 22.7 ms                                                | 24.8 ms: 1.09x slower                                      |
| deepcopy                   | 358 us                                                 | 392 us: 1.09x slower                                       |
| sqlglot_normalize          | 108 ms                                                 | 118 ms: 1.10x slower                                       |
| deepcopy_memo              | 39.1 us                                                | 43.0 us: 1.10x slower                                      |
| dulwich_log                | 64.3 ms                                                | 70.8 ms: 1.10x slower                                      |
| 2to3                       | 267 ms                                                 | 294 ms: 1.10x slower                                       |
| genshi_xml                 | 50.9 ms                                                | 56.2 ms: 1.10x slower                                      |
| deepcopy_reduce            | 3.20 us                                                | 3.53 us: 1.10x slower                                      |
| tomli_loads                | 2.14 sec                                               | 2.37 sec: 1.10x slower                                     |
| sqlglot_optimize           | 53.7 ms                                                | 59.4 ms: 1.11x slower                                      |
| logging_format             | 6.40 us                                                | 7.09 us: 1.11x slower                                      |
| pprint_pformat             | 1.49 sec                                               | 1.66 sec: 1.11x slower                                     |
| scimark_fft                | 364 ms                                                 | 405 ms: 1.11x slower                                       |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 5.61 ms: 1.11x slower                                      |
| docutils                   | 2.59 sec                                               | 2.89 sec: 1.11x slower                                     |
| hexiom                     | 6.16 ms                                                | 6.86 ms: 1.11x slower                                      |
| pprint_safe_repr           | 728 ms                                                 | 812 ms: 1.12x slower                                       |
| fannkuch                   | 404 ms                                                 | 451 ms: 1.12x slower                                       |
| html5lib                   | 64.2 ms                                                | 71.7 ms: 1.12x slower                                      |
| chameleon                  | 6.94 ms                                                | 7.76 ms: 1.12x slower                                      |
| comprehensions             | 16.5 us                                                | 18.5 us: 1.12x slower                                      |
| scimark_lu                 | 113 ms                                                 | 126 ms: 1.12x slower                                       |
| telco                      | 8.54 ms                                                | 9.60 ms: 1.12x slower                                      |
| spectral_norm              | 115 ms                                                 | 130 ms: 1.13x slower                                       |
| logging_simple             | 5.72 us                                                | 6.44 us: 1.13x slower                                      |
| scimark_monte_carlo        | 67.4 ms                                                | 76.1 ms: 1.13x slower                                      |
| pathlib                    | 17.5 ms                                                | 19.8 ms: 1.13x slower                                      |
| xml_etree_iterparse        | 101 ms                                                 | 114 ms: 1.13x slower                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.44 ms: 1.13x slower                                      |
| nqueens                    | 78.4 ms                                                | 88.6 ms: 1.13x slower                                      |
| regex_compile              | 132 ms                                                 | 149 ms: 1.13x slower                                       |
| sqlglot_transpile          | 1.58 ms                                                | 1.79 ms: 1.13x slower                                      |
| scimark_sor                | 124 ms                                                 | 140 ms: 1.13x slower                                       |
| json_loads                 | 27.2 us                                                | 30.9 us: 1.14x slower                                      |
| unpickle_pure_python       | 216 us                                                 | 246 us: 1.14x slower                                       |
| logging_silent             | 102 ns                                                 | 116 ns: 1.14x slower                                       |
| async_generators           | 436 ms                                                 | 500 ms: 1.15x slower                                       |
| sympy_integrate            | 19.9 ms                                                | 22.9 ms: 1.15x slower                                      |
| tornado_http               | 92.4 ms                                                | 108 ms: 1.16x slower                                       |
| mako                       | 11.1 ms                                                | 12.9 ms: 1.17x slower                                      |
| raytrace                   | 267 ms                                                 | 314 ms: 1.17x slower                                       |
| chaos                      | 58.1 ms                                                | 68.7 ms: 1.18x slower                                      |
| float                      | 79.2 ms                                                | 95.5 ms: 1.21x slower                                      |
| sympy_str                  | 275 ms                                                 | 332 ms: 1.21x slower                                       |
| deltablue                  | 3.23 ms                                                | 3.99 ms: 1.24x slower                                      |
| nbody                      | 87.0 ms                                                | 110 ms: 1.26x slower                                       |
| bench_thread_pool          | 822 us                                                 | 1.09 ms: 1.32x slower                                      |
| sympy_expand               | 463 ms                                                 | 613 ms: 1.32x slower                                       |
| python_startup_no_site     | 6.96 ms                                                | 9.60 ms: 1.38x slower                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 804 ms: 1.39x slower                                       |
| sympy_sum                  | 150 ms                                                 | 211 ms: 1.40x slower                                       |
| async_tree_none            | 351 ms                                                 | 509 ms: 1.45x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 657 ms: 1.49x slower                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 692 ms: 1.49x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 850 ms: 1.56x slower                                       |
| async_tree_io              | 842 ms                                                 | 1.39 sec: 1.65x slower                                     |
| async_tree_none_tg         | 321 ms                                                 | 540 ms: 1.68x slower                                       |
| async_tree_io_tg           | 857 ms                                                 | 1.45 sec: 1.70x slower                                     |
| xml_etree_parse            | 156 ms                                                 | 472 ms: 3.03x slower                                       |
| coverage                   | 84.0 ms                                                | 725 ms: 8.63x slower                                       |
| thrift                     | 809 us                                                 | 9.50 ms: 11.75x slower                                     |
| xml_etree_process          | 60.6 ms                                                | 1.03 sec: 16.96x slower                                    |
| xml_etree_generate         | 86.7 ms                                                | 1.58 sec: 18.23x slower                                    |
| Geometric mean             | (ref)                                                  | 1.28x slower                                               |

Benchmark hidden because not significant (1): mypy2
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (11) of results/bm-20231122-3.13.0a2-9c4347e-NOGIL/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.221x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.11x

# Memory
- memory change: 0.53x