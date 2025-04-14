# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b2
- machine: linux-x86_64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.013x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 274 ms: 1.03x slower                                       |
| chameleon      | 6.94 ms                                                | 7.22 ms: 1.04x slower                                      |
| docutils       | 2.59 sec                                               | 2.83 sec: 1.09x slower                                     |
| html5lib       | 64.2 ms                                                | 67.2 ms: 1.05x slower                                      |
| tornado_http   | 92.4 ms                                                | 94.6 ms: 1.02x slower                                      |
| Geometric mean | (ref)                                                  | 1.05x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 444 ms: 1.04x faster                                       |
| async_generators           | 436 ms                                                 | 442 ms: 1.01x slower                                       |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                      |
| asyncio_websockets         | 552 ms                                                 | 567 ms: 1.03x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 463 ms: 1.05x slower                                       |
| async_tree_none_tg         | 321 ms                                                 | 336 ms: 1.05x slower                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 611 ms: 1.06x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 587 ms: 1.08x slower                                       |
| async_tree_none            | 351 ms                                                 | 378 ms: 1.08x slower                                       |
| async_tree_io_tg           | 857 ms                                                 | 936 ms: 1.09x slower                                       |
| async_tree_io              | 842 ms                                                 | 939 ms: 1.12x slower                                       |
| Geometric mean             | (ref)                                                  | 1.05x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 88.3 ms: 1.02x slower                                      |
| pidigits       | 186 ms                                                 | 191 ms: 1.03x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.1 ms: 1.04x faster                                      |
| regex_effbot   | 3.73 ms                                                | 3.67 ms: 1.02x faster                                      |
| regex_dna      | 218 ms                                                 | 221 ms: 1.01x slower                                       |
| regex_compile  | 132 ms                                                 | 137 ms: 1.03x slower                                       |
| Geometric mean | (ref)                                                  | 1.00x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 310 us                                                 | 305 us: 1.02x faster                                       |
| tomli_loads          | 2.14 sec                                               | 2.12 sec: 1.01x faster                                     |
| xml_etree_generate   | 86.7 ms                                                | 87.4 ms: 1.01x slower                                      |
| xml_etree_process    | 60.6 ms                                                | 61.2 ms: 1.01x slower                                      |
| unpickle_pure_python | 216 us                                                 | 218 us: 1.01x slower                                       |
| json_dumps           | 10.6 ms                                                | 10.7 ms: 1.02x slower                                      |
| xml_etree_parse      | 156 ms                                                 | 162 ms: 1.04x slower                                       |
| xml_etree_iterparse  | 101 ms                                                 | 107 ms: 1.06x slower                                       |
| json_loads           | 27.2 us                                                | 28.9 us: 1.06x slower                                      |
| Geometric mean       | (ref)                                                  | 1.02x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.8 ms: 1.16x faster                                      |
| python_startup_no_site | 6.96 ms                                                | 7.11 ms: 1.02x slower                                      |
| Geometric mean         | (ref)                                                  | 1.07x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 35.2 ms                                                | 34.8 ms: 1.01x faster                                      |
| genshi_text     | 23.5 ms                                                | 23.7 ms: 1.01x slower                                      |
| genshi_xml      | 50.9 ms                                                | 51.6 ms: 1.01x slower                                      |
| mako            | 11.1 ms                                                | 11.2 ms: 1.01x slower                                      |
| Geometric mean  | (ref)                                                  | 1.01x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mypy2                      | 1.04 sec                                               | 742 ms: 1.41x faster                                       |
| create_gc_cycles           | 2.41 ms                                                | 1.82 ms: 1.33x faster                                      |
| python_startup             | 12.5 ms                                                | 10.8 ms: 1.16x faster                                      |
| gc_traversal               | 4.37 ms                                                | 3.98 ms: 1.10x faster                                      |
| async_tree_memoization_tg  | 464 ms                                                 | 444 ms: 1.04x faster                                       |
| regex_v8                   | 26.2 ms                                                | 25.1 ms: 1.04x faster                                      |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                     |
| pickle_pure_python         | 310 us                                                 | 305 us: 1.02x faster                                       |
| regex_effbot               | 3.73 ms                                                | 3.67 ms: 1.02x faster                                      |
| telco                      | 8.54 ms                                                | 8.41 ms: 1.02x faster                                      |
| pathlib                    | 17.5 ms                                                | 17.3 ms: 1.01x faster                                      |
| django_template            | 35.2 ms                                                | 34.8 ms: 1.01x faster                                      |
| json                       | 5.36 ms                                                | 5.31 ms: 1.01x faster                                      |
| tomli_loads                | 2.14 sec                                               | 2.12 sec: 1.01x faster                                     |
| go                         | 144 ms                                                 | 145 ms: 1.01x slower                                       |
| genshi_text                | 23.5 ms                                                | 23.7 ms: 1.01x slower                                      |
| spectral_norm              | 115 ms                                                 | 116 ms: 1.01x slower                                       |
| xml_etree_generate         | 86.7 ms                                                | 87.4 ms: 1.01x slower                                      |
| comprehensions             | 16.5 us                                                | 16.6 us: 1.01x slower                                      |
| deltablue                  | 3.23 ms                                                | 3.25 ms: 1.01x slower                                      |
| xml_etree_process          | 60.6 ms                                                | 61.2 ms: 1.01x slower                                      |
| meteor_contest             | 109 ms                                                 | 110 ms: 1.01x slower                                       |
| unpickle_pure_python       | 216 us                                                 | 218 us: 1.01x slower                                       |
| logging_format             | 6.40 us                                                | 6.47 us: 1.01x slower                                      |
| regex_dna                  | 218 ms                                                 | 221 ms: 1.01x slower                                       |
| genshi_xml                 | 50.9 ms                                                | 51.6 ms: 1.01x slower                                      |
| mako                       | 11.1 ms                                                | 11.2 ms: 1.01x slower                                      |
| async_generators           | 436 ms                                                 | 442 ms: 1.01x slower                                       |
| bench_thread_pool          | 822 us                                                 | 834 us: 1.01x slower                                       |
| nbody                      | 87.0 ms                                                | 88.3 ms: 1.02x slower                                      |
| json_dumps                 | 10.6 ms                                                | 10.7 ms: 1.02x slower                                      |
| deepcopy_memo              | 39.1 us                                                | 39.7 us: 1.02x slower                                      |
| thrift                     | 809 us                                                 | 823 us: 1.02x slower                                       |
| sympy_expand               | 463 ms                                                 | 473 ms: 1.02x slower                                       |
| python_startup_no_site     | 6.96 ms                                                | 7.11 ms: 1.02x slower                                      |
| hexiom                     | 6.16 ms                                                | 6.30 ms: 1.02x slower                                      |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                      |
| generators                 | 29.0 ms                                                | 29.6 ms: 1.02x slower                                      |
| tornado_http               | 92.4 ms                                                | 94.6 ms: 1.02x slower                                      |
| sqlglot_normalize          | 108 ms                                                 | 110 ms: 1.02x slower                                       |
| mdp                        | 2.72 sec                                               | 2.79 sec: 1.02x slower                                     |
| deepcopy                   | 358 us                                                 | 367 us: 1.02x slower                                       |
| scimark_monte_carlo        | 67.4 ms                                                | 69.2 ms: 1.03x slower                                      |
| pidigits                   | 186 ms                                                 | 191 ms: 1.03x slower                                       |
| asyncio_websockets         | 552 ms                                                 | 567 ms: 1.03x slower                                       |
| 2to3                       | 267 ms                                                 | 274 ms: 1.03x slower                                       |
| sympy_str                  | 275 ms                                                 | 282 ms: 1.03x slower                                       |
| pyflate                    | 471 ms                                                 | 484 ms: 1.03x slower                                       |
| crypto_pyaes               | 75.3 ms                                                | 77.5 ms: 1.03x slower                                      |
| logging_silent             | 102 ns                                                 | 105 ns: 1.03x slower                                       |
| sympy_integrate            | 19.9 ms                                                | 20.5 ms: 1.03x slower                                      |
| scimark_sor                | 124 ms                                                 | 127 ms: 1.03x slower                                       |
| sqlglot_transpile          | 1.58 ms                                                | 1.63 ms: 1.03x slower                                      |
| sqlglot_optimize           | 53.7 ms                                                | 55.5 ms: 1.03x slower                                      |
| regex_compile              | 132 ms                                                 | 137 ms: 1.03x slower                                       |
| sympy_sum                  | 150 ms                                                 | 156 ms: 1.04x slower                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.04x slower                                      |
| nqueens                    | 78.4 ms                                                | 81.4 ms: 1.04x slower                                      |
| xml_etree_parse            | 156 ms                                                 | 162 ms: 1.04x slower                                       |
| chameleon                  | 6.94 ms                                                | 7.22 ms: 1.04x slower                                      |
| pprint_pformat             | 1.49 sec                                               | 1.56 sec: 1.04x slower                                     |
| pprint_safe_repr           | 728 ms                                                 | 758 ms: 1.04x slower                                       |
| dulwich_log                | 64.3 ms                                                | 67.2 ms: 1.04x slower                                      |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 5.27 ms: 1.04x slower                                      |
| richards                   | 48.7 ms                                                | 50.9 ms: 1.05x slower                                      |
| richards_super             | 54.9 ms                                                | 57.4 ms: 1.05x slower                                      |
| deepcopy_reduce            | 3.20 us                                                | 3.35 us: 1.05x slower                                      |
| html5lib                   | 64.2 ms                                                | 67.2 ms: 1.05x slower                                      |
| async_tree_memoization     | 442 ms                                                 | 463 ms: 1.05x slower                                       |
| async_tree_none_tg         | 321 ms                                                 | 336 ms: 1.05x slower                                       |
| chaos                      | 58.1 ms                                                | 61.3 ms: 1.06x slower                                      |
| bpe_tokeniser              | 4.75 sec                                               | 5.02 sec: 1.06x slower                                     |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 611 ms: 1.06x slower                                       |
| xml_etree_iterparse        | 101 ms                                                 | 107 ms: 1.06x slower                                       |
| json_loads                 | 27.2 us                                                | 28.9 us: 1.06x slower                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 587 ms: 1.08x slower                                       |
| scimark_fft                | 364 ms                                                 | 392 ms: 1.08x slower                                       |
| scimark_lu                 | 113 ms                                                 | 122 ms: 1.08x slower                                       |
| async_tree_none            | 351 ms                                                 | 378 ms: 1.08x slower                                       |
| docutils                   | 2.59 sec                                               | 2.83 sec: 1.09x slower                                     |
| async_tree_io_tg           | 857 ms                                                 | 936 ms: 1.09x slower                                       |
| coverage                   | 84.0 ms                                                | 93.1 ms: 1.11x slower                                      |
| async_tree_io              | 842 ms                                                 | 939 ms: 1.12x slower                                       |
| Geometric mean             | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (7): fannkuch, bench_mp_pool, float, raytrace, typing_runtime_protocols, logging_simple, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.013x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 0.91x