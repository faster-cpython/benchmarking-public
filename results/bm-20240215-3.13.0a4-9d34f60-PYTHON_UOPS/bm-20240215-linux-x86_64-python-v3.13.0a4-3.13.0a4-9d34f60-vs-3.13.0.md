# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.035x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 277 ms: 1.04x slower                                       |
| docutils       | 2.59 sec                                               | 2.64 sec: 1.02x slower                                     |
| html5lib       | 64.2 ms                                                | 67.3 ms: 1.05x slower                                      |
| tornado_http   | 92.4 ms                                                | 96.9 ms: 1.05x slower                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_generators           | 436 ms                                                 | 455 ms: 1.04x slower                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 710 ms: 1.23x slower                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 576 ms: 1.24x slower                                       |
| async_tree_none            | 351 ms                                                 | 438 ms: 1.25x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 565 ms: 1.28x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 723 ms: 1.32x slower                                       |
| async_tree_none_tg         | 321 ms                                                 | 448 ms: 1.40x slower                                       |
| async_tree_io              | 842 ms                                                 | 1.18 sec: 1.40x slower                                     |
| async_tree_io_tg           | 857 ms                                                 | 1.20 sec: 1.41x slower                                     |
| Geometric mean             | (ref)                                                  | 1.22x slower                                               |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                       |
| float          | 79.2 ms                                                | 85.3 ms: 1.08x slower                                      |
| nbody          | 87.0 ms                                                | 103 ms: 1.19x slower                                       |
| Geometric mean | (ref)                                                  | 1.09x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.2 ms: 1.04x faster                                      |
| regex_effbot   | 3.73 ms                                                | 3.59 ms: 1.04x faster                                      |
| regex_dna      | 218 ms                                                 | 216 ms: 1.01x faster                                       |
| regex_compile  | 132 ms                                                 | 138 ms: 1.04x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 310 us                                                 | 298 us: 1.04x faster                                       |
| xml_etree_process    | 60.6 ms                                                | 58.4 ms: 1.04x faster                                      |
| json_dumps           | 10.6 ms                                                | 10.4 ms: 1.02x faster                                      |
| xml_etree_generate   | 86.7 ms                                                | 86.0 ms: 1.01x faster                                      |
| json_loads           | 27.2 us                                                | 27.5 us: 1.01x slower                                      |
| tomli_loads          | 2.14 sec                                               | 2.21 sec: 1.03x slower                                     |
| xml_etree_iterparse  | 101 ms                                                 | 107 ms: 1.06x slower                                       |
| unpickle_pure_python | 216 us                                                 | 230 us: 1.06x slower                                       |
| Geometric mean       | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.2 ms: 1.22x faster                                      |
| python_startup_no_site | 6.96 ms                                                | 8.84 ms: 1.27x slower                                      |
| Geometric mean         | (ref)                                                  | 1.02x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 35.2 ms                                                | 34.2 ms: 1.03x faster                                      |
| genshi_text     | 23.5 ms                                                | 23.4 ms: 1.01x faster                                      |
| genshi_xml      | 50.9 ms                                                | 52.7 ms: 1.03x slower                                      |
| mako            | 11.1 ms                                                | 12.1 ms: 1.09x slower                                      |
| Geometric mean  | (ref)                                                  | 1.02x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles           | 2.41 ms                                                | 1.48 ms: 1.63x faster                                      |
| typing_runtime_protocols   | 165 us                                                 | 111 us: 1.48x faster                                       |
| python_startup             | 12.5 ms                                                | 10.2 ms: 1.22x faster                                      |
| mypy2                      | 1.04 sec                                               | 865 ms: 1.21x faster                                       |
| gc_traversal               | 4.37 ms                                                | 3.72 ms: 1.18x faster                                      |
| richards                   | 48.7 ms                                                | 45.3 ms: 1.08x faster                                      |
| richards_super             | 54.9 ms                                                | 51.7 ms: 1.06x faster                                      |
| json                       | 5.36 ms                                                | 5.07 ms: 1.06x faster                                      |
| deepcopy_reduce            | 3.20 us                                                | 3.03 us: 1.06x faster                                      |
| pickle_pure_python         | 310 us                                                 | 298 us: 1.04x faster                                       |
| regex_v8                   | 26.2 ms                                                | 25.2 ms: 1.04x faster                                      |
| regex_effbot               | 3.73 ms                                                | 3.59 ms: 1.04x faster                                      |
| xml_etree_process          | 60.6 ms                                                | 58.4 ms: 1.04x faster                                      |
| scimark_sor                | 124 ms                                                 | 119 ms: 1.04x faster                                       |
| django_template            | 35.2 ms                                                | 34.2 ms: 1.03x faster                                      |
| thrift                     | 809 us                                                 | 789 us: 1.03x faster                                       |
| deepcopy                   | 358 us                                                 | 350 us: 1.02x faster                                       |
| json_dumps                 | 10.6 ms                                                | 10.4 ms: 1.02x faster                                      |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                     |
| deepcopy_memo              | 39.1 us                                                | 38.5 us: 1.02x faster                                      |
| telco                      | 8.54 ms                                                | 8.42 ms: 1.01x faster                                      |
| regex_dna                  | 218 ms                                                 | 216 ms: 1.01x faster                                       |
| xml_etree_generate         | 86.7 ms                                                | 86.0 ms: 1.01x faster                                      |
| genshi_text                | 23.5 ms                                                | 23.4 ms: 1.01x faster                                      |
| logging_silent             | 102 ns                                                 | 101 ns: 1.01x faster                                       |
| mdp                        | 2.72 sec                                               | 2.71 sec: 1.00x faster                                     |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.00x faster                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                      |
| sqlglot_normalize          | 108 ms                                                 | 108 ms: 1.01x slower                                       |
| generators                 | 29.0 ms                                                | 29.2 ms: 1.01x slower                                      |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                       |
| json_loads                 | 27.2 us                                                | 27.5 us: 1.01x slower                                      |
| logging_format             | 6.40 us                                                | 6.47 us: 1.01x slower                                      |
| scimark_fft                | 364 ms                                                 | 369 ms: 1.01x slower                                       |
| logging_simple             | 5.72 us                                                | 5.81 us: 1.02x slower                                      |
| docutils                   | 2.59 sec                                               | 2.64 sec: 1.02x slower                                     |
| sqlglot_transpile          | 1.58 ms                                                | 1.61 ms: 1.02x slower                                      |
| bench_thread_pool          | 822 us                                                 | 839 us: 1.02x slower                                       |
| sympy_str                  | 275 ms                                                 | 283 ms: 1.03x slower                                       |
| go                         | 144 ms                                                 | 148 ms: 1.03x slower                                       |
| tomli_loads                | 2.14 sec                                               | 2.21 sec: 1.03x slower                                     |
| sympy_integrate            | 19.9 ms                                                | 20.6 ms: 1.03x slower                                      |
| genshi_xml                 | 50.9 ms                                                | 52.7 ms: 1.03x slower                                      |
| sqlglot_optimize           | 53.7 ms                                                | 55.7 ms: 1.04x slower                                      |
| scimark_lu                 | 113 ms                                                 | 117 ms: 1.04x slower                                       |
| 2to3                       | 267 ms                                                 | 277 ms: 1.04x slower                                       |
| fannkuch                   | 404 ms                                                 | 420 ms: 1.04x slower                                       |
| regex_compile              | 132 ms                                                 | 138 ms: 1.04x slower                                       |
| crypto_pyaes               | 75.3 ms                                                | 78.6 ms: 1.04x slower                                      |
| raytrace                   | 267 ms                                                 | 279 ms: 1.04x slower                                       |
| async_generators           | 436 ms                                                 | 455 ms: 1.04x slower                                       |
| deltablue                  | 3.23 ms                                                | 3.37 ms: 1.04x slower                                      |
| sympy_expand               | 463 ms                                                 | 484 ms: 1.05x slower                                       |
| tornado_http               | 92.4 ms                                                | 96.9 ms: 1.05x slower                                      |
| pathlib                    | 17.5 ms                                                | 18.4 ms: 1.05x slower                                      |
| html5lib                   | 64.2 ms                                                | 67.3 ms: 1.05x slower                                      |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 5.30 ms: 1.05x slower                                      |
| sympy_sum                  | 150 ms                                                 | 159 ms: 1.05x slower                                       |
| xml_etree_iterparse        | 101 ms                                                 | 107 ms: 1.06x slower                                       |
| pprint_safe_repr           | 728 ms                                                 | 770 ms: 1.06x slower                                       |
| unpickle_pure_python       | 216 us                                                 | 230 us: 1.06x slower                                       |
| dulwich_log                | 64.3 ms                                                | 68.7 ms: 1.07x slower                                      |
| pyflate                    | 471 ms                                                 | 507 ms: 1.08x slower                                       |
| float                      | 79.2 ms                                                | 85.3 ms: 1.08x slower                                      |
| bpe_tokeniser              | 4.75 sec                                               | 5.15 sec: 1.09x slower                                     |
| mako                       | 11.1 ms                                                | 12.1 ms: 1.09x slower                                      |
| pprint_pformat             | 1.49 sec                                               | 1.63 sec: 1.09x slower                                     |
| scimark_monte_carlo        | 67.4 ms                                                | 74.5 ms: 1.10x slower                                      |
| comprehensions             | 16.5 us                                                | 18.3 us: 1.11x slower                                      |
| coverage                   | 84.0 ms                                                | 94.7 ms: 1.13x slower                                      |
| spectral_norm              | 115 ms                                                 | 132 ms: 1.14x slower                                       |
| nqueens                    | 78.4 ms                                                | 91.0 ms: 1.16x slower                                      |
| nbody                      | 87.0 ms                                                | 103 ms: 1.19x slower                                       |
| chaos                      | 58.1 ms                                                | 69.5 ms: 1.20x slower                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 710 ms: 1.23x slower                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 576 ms: 1.24x slower                                       |
| async_tree_none            | 351 ms                                                 | 438 ms: 1.25x slower                                       |
| hexiom                     | 6.16 ms                                                | 7.76 ms: 1.26x slower                                      |
| python_startup_no_site     | 6.96 ms                                                | 8.84 ms: 1.27x slower                                      |
| async_tree_memoization     | 442 ms                                                 | 565 ms: 1.28x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 723 ms: 1.32x slower                                       |
| async_tree_none_tg         | 321 ms                                                 | 448 ms: 1.40x slower                                       |
| async_tree_io              | 842 ms                                                 | 1.18 sec: 1.40x slower                                     |
| async_tree_io_tg           | 857 ms                                                 | 1.20 sec: 1.41x slower                                     |
| Geometric mean             | (ref)                                                  | 1.04x slower                                               |

Benchmark hidden because not significant (6): pylint, coroutines, chameleon, bench_mp_pool, asyncio_websockets, xml_etree_parse
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240215-3.13.0a4-9d34f60-PYTHON_UOPS/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.035x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 0.91x