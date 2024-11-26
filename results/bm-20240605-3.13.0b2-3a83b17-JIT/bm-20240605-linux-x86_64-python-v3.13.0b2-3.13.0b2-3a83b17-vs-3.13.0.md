# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b2
- machine: linux-x86_64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.005x slower
- HPT reliability: 98.25%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 281 ms: 1.05x slower                                       |
| chameleon      | 6.94 ms                                                | 7.11 ms: 1.03x slower                                      |
| docutils       | 2.59 sec                                               | 2.99 sec: 1.15x slower                                     |
| html5lib       | 64.2 ms                                                | 69.1 ms: 1.08x slower                                      |
| tornado_http   | 92.4 ms                                                | 96.9 ms: 1.05x slower                                      |
| Geometric mean | (ref)                                                  | 1.07x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 441 ms: 1.05x faster                                       |
| asyncio_websockets         | 552 ms                                                 | 567 ms: 1.03x slower                                       |
| async_tree_none_tg         | 321 ms                                                 | 333 ms: 1.04x slower                                       |
| async_generators           | 436 ms                                                 | 462 ms: 1.06x slower                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 612 ms: 1.06x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 584 ms: 1.07x slower                                       |
| async_tree_none            | 351 ms                                                 | 377 ms: 1.08x slower                                       |
| async_tree_io_tg           | 857 ms                                                 | 945 ms: 1.10x slower                                       |
| async_tree_io              | 842 ms                                                 | 932 ms: 1.11x slower                                       |
| Geometric mean             | (ref)                                                  | 1.05x slower                                               |

Benchmark hidden because not significant (2): coroutines, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 79.2 ms                                                | 73.0 ms: 1.08x faster                                      |
| nbody          | 87.0 ms                                                | 83.5 ms: 1.04x faster                                      |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.2 ms: 1.04x faster                                      |
| regex_effbot   | 3.73 ms                                                | 3.69 ms: 1.01x faster                                      |
| regex_compile  | 132 ms                                                 | 138 ms: 1.05x slower                                       |
| regex_dna      | 218 ms                                                 | 230 ms: 1.05x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 1.95 sec: 1.10x faster                                     |
| xml_etree_generate   | 86.7 ms                                                | 82.9 ms: 1.05x faster                                      |
| xml_etree_parse      | 156 ms                                                 | 149 ms: 1.04x faster                                       |
| xml_etree_process    | 60.6 ms                                                | 58.5 ms: 1.04x faster                                      |
| pickle_pure_python   | 310 us                                                 | 300 us: 1.04x faster                                       |
| json_dumps           | 10.6 ms                                                | 10.3 ms: 1.02x faster                                      |
| unpickle_pure_python | 216 us                                                 | 222 us: 1.03x slower                                       |
| json_loads           | 27.2 us                                                | 28.8 us: 1.06x slower                                      |
| Geometric mean       | (ref)                                                  | 1.02x faster                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 11.3 ms: 1.11x faster                                      |
| python_startup_no_site | 6.96 ms                                                | 7.62 ms: 1.10x slower                                      |
| Geometric mean         | (ref)                                                  | 1.01x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.83 ms: 1.13x faster                                      |
| django_template | 35.2 ms                                                | 36.4 ms: 1.03x slower                                      |
| genshi_text     | 23.5 ms                                                | 25.5 ms: 1.08x slower                                      |
| genshi_xml      | 50.9 ms                                                | 60.2 ms: 1.18x slower                                      |
| Geometric mean  | (ref)                                                  | 1.04x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles           | 2.41 ms                                                | 1.83 ms: 1.31x faster                                      |
| mypy2                      | 1.04 sec                                               | 814 ms: 1.28x faster                                       |
| richards                   | 48.7 ms                                                | 41.7 ms: 1.17x faster                                      |
| scimark_fft                | 364 ms                                                 | 317 ms: 1.15x faster                                       |
| richards_super             | 54.9 ms                                                | 48.4 ms: 1.13x faster                                      |
| fannkuch                   | 404 ms                                                 | 358 ms: 1.13x faster                                       |
| mako                       | 11.1 ms                                                | 9.83 ms: 1.13x faster                                      |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                       |
| gc_traversal               | 4.37 ms                                                | 3.88 ms: 1.13x faster                                      |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.48 ms: 1.13x faster                                      |
| crypto_pyaes               | 75.3 ms                                                | 68.0 ms: 1.11x faster                                      |
| python_startup             | 12.5 ms                                                | 11.3 ms: 1.11x faster                                      |
| tomli_loads                | 2.14 sec                                               | 1.95 sec: 1.10x faster                                     |
| float                      | 79.2 ms                                                | 73.0 ms: 1.08x faster                                      |
| pyflate                    | 471 ms                                                 | 436 ms: 1.08x faster                                       |
| scimark_monte_carlo        | 67.4 ms                                                | 62.7 ms: 1.07x faster                                      |
| telco                      | 8.54 ms                                                | 8.12 ms: 1.05x faster                                      |
| async_tree_memoization_tg  | 464 ms                                                 | 441 ms: 1.05x faster                                       |
| deepcopy_memo              | 39.1 us                                                | 37.3 us: 1.05x faster                                      |
| xml_etree_generate         | 86.7 ms                                                | 82.9 ms: 1.05x faster                                      |
| xml_etree_parse            | 156 ms                                                 | 149 ms: 1.04x faster                                       |
| nbody                      | 87.0 ms                                                | 83.5 ms: 1.04x faster                                      |
| regex_v8                   | 26.2 ms                                                | 25.2 ms: 1.04x faster                                      |
| xml_etree_process          | 60.6 ms                                                | 58.5 ms: 1.04x faster                                      |
| mdp                        | 2.72 sec                                               | 2.62 sec: 1.04x faster                                     |
| pickle_pure_python         | 310 us                                                 | 300 us: 1.04x faster                                       |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                     |
| pprint_pformat             | 1.49 sec                                               | 1.45 sec: 1.03x faster                                     |
| json_dumps                 | 10.6 ms                                                | 10.3 ms: 1.02x faster                                      |
| pprint_safe_repr           | 728 ms                                                 | 715 ms: 1.02x faster                                       |
| logging_format             | 6.40 us                                                | 6.30 us: 1.01x faster                                      |
| regex_effbot               | 3.73 ms                                                | 3.69 ms: 1.01x faster                                      |
| pathlib                    | 17.5 ms                                                | 17.4 ms: 1.01x faster                                      |
| chaos                      | 58.1 ms                                                | 58.5 ms: 1.01x slower                                      |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                       |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.30 ms: 1.02x slower                                      |
| meteor_contest             | 109 ms                                                 | 111 ms: 1.02x slower                                       |
| thrift                     | 809 us                                                 | 826 us: 1.02x slower                                       |
| chameleon                  | 6.94 ms                                                | 7.11 ms: 1.03x slower                                      |
| asyncio_websockets         | 552 ms                                                 | 567 ms: 1.03x slower                                       |
| sqlglot_transpile          | 1.58 ms                                                | 1.63 ms: 1.03x slower                                      |
| bpe_tokeniser              | 4.75 sec                                               | 4.88 sec: 1.03x slower                                     |
| unpickle_pure_python       | 216 us                                                 | 222 us: 1.03x slower                                       |
| deepcopy_reduce            | 3.20 us                                                | 3.30 us: 1.03x slower                                      |
| django_template            | 35.2 ms                                                | 36.4 ms: 1.03x slower                                      |
| scimark_sor                | 124 ms                                                 | 128 ms: 1.04x slower                                       |
| async_tree_none_tg         | 321 ms                                                 | 333 ms: 1.04x slower                                       |
| deepcopy                   | 358 us                                                 | 375 us: 1.05x slower                                       |
| regex_compile              | 132 ms                                                 | 138 ms: 1.05x slower                                       |
| raytrace                   | 267 ms                                                 | 280 ms: 1.05x slower                                       |
| tornado_http               | 92.4 ms                                                | 96.9 ms: 1.05x slower                                      |
| go                         | 144 ms                                                 | 151 ms: 1.05x slower                                       |
| typing_runtime_protocols   | 165 us                                                 | 173 us: 1.05x slower                                       |
| regex_dna                  | 218 ms                                                 | 230 ms: 1.05x slower                                       |
| 2to3                       | 267 ms                                                 | 281 ms: 1.05x slower                                       |
| sqlglot_normalize          | 108 ms                                                 | 114 ms: 1.06x slower                                       |
| bench_thread_pool          | 822 us                                                 | 867 us: 1.06x slower                                       |
| logging_silent             | 102 ns                                                 | 108 ns: 1.06x slower                                       |
| sqlglot_optimize           | 53.7 ms                                                | 56.8 ms: 1.06x slower                                      |
| json_loads                 | 27.2 us                                                | 28.8 us: 1.06x slower                                      |
| async_generators           | 436 ms                                                 | 462 ms: 1.06x slower                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 612 ms: 1.06x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 584 ms: 1.07x slower                                       |
| async_tree_none            | 351 ms                                                 | 377 ms: 1.08x slower                                       |
| html5lib                   | 64.2 ms                                                | 69.1 ms: 1.08x slower                                      |
| genshi_text                | 23.5 ms                                                | 25.5 ms: 1.08x slower                                      |
| hexiom                     | 6.16 ms                                                | 6.67 ms: 1.08x slower                                      |
| dulwich_log                | 64.3 ms                                                | 69.7 ms: 1.08x slower                                      |
| python_startup_no_site     | 6.96 ms                                                | 7.62 ms: 1.10x slower                                      |
| sympy_str                  | 275 ms                                                 | 302 ms: 1.10x slower                                       |
| sympy_expand               | 463 ms                                                 | 510 ms: 1.10x slower                                       |
| coverage                   | 84.0 ms                                                | 92.7 ms: 1.10x slower                                      |
| async_tree_io_tg           | 857 ms                                                 | 945 ms: 1.10x slower                                       |
| nqueens                    | 78.4 ms                                                | 86.5 ms: 1.10x slower                                      |
| async_tree_io              | 842 ms                                                 | 932 ms: 1.11x slower                                       |
| pylint                     | 313 ms                                                 | 353 ms: 1.13x slower                                       |
| scimark_lu                 | 113 ms                                                 | 127 ms: 1.13x slower                                       |
| sympy_integrate            | 19.9 ms                                                | 22.5 ms: 1.13x slower                                      |
| sympy_sum                  | 150 ms                                                 | 172 ms: 1.14x slower                                       |
| deltablue                  | 3.23 ms                                                | 3.70 ms: 1.15x slower                                      |
| docutils                   | 2.59 sec                                               | 2.99 sec: 1.15x slower                                     |
| generators                 | 29.0 ms                                                | 33.5 ms: 1.16x slower                                      |
| genshi_xml                 | 50.9 ms                                                | 60.2 ms: 1.18x slower                                      |
| Geometric mean             | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (6): coroutines, logging_simple, json, bench_mp_pool, xml_etree_iterparse, async_tree_memoization
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.005x slower
# HPT report

- Reliability score: 98.25% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x