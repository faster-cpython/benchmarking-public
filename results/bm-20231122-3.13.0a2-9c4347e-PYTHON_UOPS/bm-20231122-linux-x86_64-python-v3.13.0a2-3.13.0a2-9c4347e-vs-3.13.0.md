# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a2
- machine: linux-x86_64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.089x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: 0.86x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 288 ms: 1.08x slower                                       |
| chameleon      | 6.94 ms                                                | 7.54 ms: 1.09x slower                                      |
| docutils       | 2.59 sec                                               | 2.73 sec: 1.05x slower                                     |
| tornado_http   | 92.4 ms                                                | 99.5 ms: 1.08x slower                                      |
| Geometric mean | (ref)                                                  | 1.07x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| coroutines                 | 22.7 ms                                                | 22.4 ms: 1.01x faster                                      |
| async_generators           | 436 ms                                                 | 457 ms: 1.05x slower                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 731 ms: 1.27x slower                                       |
| async_tree_none            | 351 ms                                                 | 456 ms: 1.30x slower                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 611 ms: 1.32x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 583 ms: 1.32x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 760 ms: 1.39x slower                                       |
| async_tree_io              | 842 ms                                                 | 1.22 sec: 1.45x slower                                     |
| async_tree_io_tg           | 857 ms                                                 | 1.25 sec: 1.46x slower                                     |
| async_tree_none_tg         | 321 ms                                                 | 471 ms: 1.47x slower                                       |
| Geometric mean             | (ref)                                                  | 1.26x slower                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 196 ms: 1.05x slower                                       |
| float          | 79.2 ms                                                | 92.4 ms: 1.17x slower                                      |
| nbody          | 87.0 ms                                                | 119 ms: 1.36x slower                                       |
| Geometric mean | (ref)                                                  | 1.19x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.9 ms: 1.01x faster                                      |
| regex_dna      | 218 ms                                                 | 224 ms: 1.02x slower                                       |
| regex_compile  | 132 ms                                                 | 157 ms: 1.19x slower                                       |
| Geometric mean | (ref)                                                  | 1.05x slower                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 310 us                                                 | 308 us: 1.01x faster                                       |
| xml_etree_parse      | 156 ms                                                 | 158 ms: 1.02x slower                                       |
| xml_etree_process    | 60.6 ms                                                | 61.8 ms: 1.02x slower                                      |
| json_loads           | 27.2 us                                                | 28.2 us: 1.04x slower                                      |
| xml_etree_generate   | 86.7 ms                                                | 90.2 ms: 1.04x slower                                      |
| xml_etree_iterparse  | 101 ms                                                 | 112 ms: 1.10x slower                                       |
| unpickle_pure_python | 216 us                                                 | 240 us: 1.11x slower                                       |
| tomli_loads          | 2.14 sec                                               | 2.39 sec: 1.12x slower                                     |
| Geometric mean       | (ref)                                                  | 1.05x slower                                               |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.3 ms: 1.21x faster                                      |
| python_startup_no_site | 6.96 ms                                                | 9.00 ms: 1.29x slower                                      |
| Geometric mean         | (ref)                                                  | 1.04x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 11.1 ms                                                | 13.7 ms: 1.24x slower                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles           | 2.41 ms                                                | 1.46 ms: 1.65x faster                                      |
| typing_runtime_protocols   | 165 us                                                 | 122 us: 1.35x faster                                       |
| python_startup             | 12.5 ms                                                | 10.3 ms: 1.21x faster                                      |
| mypy2                      | 1.04 sec                                               | 869 ms: 1.20x faster                                       |
| json                       | 5.36 ms                                                | 5.22 ms: 1.03x faster                                      |
| gc_traversal               | 4.37 ms                                                | 4.29 ms: 1.02x faster                                      |
| regex_v8                   | 26.2 ms                                                | 25.9 ms: 1.01x faster                                      |
| coroutines                 | 22.7 ms                                                | 22.4 ms: 1.01x faster                                      |
| telco                      | 8.54 ms                                                | 8.46 ms: 1.01x faster                                      |
| deepcopy_reduce            | 3.20 us                                                | 3.18 us: 1.01x faster                                      |
| pickle_pure_python         | 310 us                                                 | 308 us: 1.01x faster                                       |
| deepcopy                   | 358 us                                                 | 362 us: 1.01x slower                                       |
| xml_etree_parse            | 156 ms                                                 | 158 ms: 1.02x slower                                       |
| xml_etree_process          | 60.6 ms                                                | 61.8 ms: 1.02x slower                                      |
| generators                 | 29.0 ms                                                | 29.6 ms: 1.02x slower                                      |
| richards                   | 48.7 ms                                                | 49.8 ms: 1.02x slower                                      |
| regex_dna                  | 218 ms                                                 | 224 ms: 1.02x slower                                       |
| mdp                        | 2.72 sec                                               | 2.79 sec: 1.03x slower                                     |
| json_loads                 | 27.2 us                                                | 28.2 us: 1.04x slower                                      |
| bench_thread_pool          | 822 us                                                 | 854 us: 1.04x slower                                       |
| xml_etree_generate         | 86.7 ms                                                | 90.2 ms: 1.04x slower                                      |
| richards_super             | 54.9 ms                                                | 57.2 ms: 1.04x slower                                      |
| pycparser                  | 1.20 sec                                               | 1.26 sec: 1.05x slower                                     |
| deepcopy_memo              | 39.1 us                                                | 41.0 us: 1.05x slower                                      |
| async_generators           | 436 ms                                                 | 457 ms: 1.05x slower                                       |
| pidigits                   | 186 ms                                                 | 196 ms: 1.05x slower                                       |
| docutils                   | 2.59 sec                                               | 2.73 sec: 1.05x slower                                     |
| logging_simple             | 5.72 us                                                | 6.03 us: 1.05x slower                                      |
| logging_silent             | 102 ns                                                 | 108 ns: 1.06x slower                                       |
| sympy_sum                  | 150 ms                                                 | 160 ms: 1.06x slower                                       |
| scimark_lu                 | 113 ms                                                 | 120 ms: 1.06x slower                                       |
| meteor_contest             | 109 ms                                                 | 116 ms: 1.06x slower                                       |
| sympy_expand               | 463 ms                                                 | 493 ms: 1.06x slower                                       |
| sympy_integrate            | 19.9 ms                                                | 21.3 ms: 1.07x slower                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.36 ms: 1.07x slower                                      |
| sqlglot_transpile          | 1.58 ms                                                | 1.70 ms: 1.07x slower                                      |
| sympy_str                  | 275 ms                                                 | 294 ms: 1.07x slower                                       |
| dulwich_log                | 64.3 ms                                                | 69.0 ms: 1.07x slower                                      |
| logging_format             | 6.40 us                                                | 6.86 us: 1.07x slower                                      |
| sqlglot_normalize          | 108 ms                                                 | 115 ms: 1.07x slower                                       |
| tornado_http               | 92.4 ms                                                | 99.5 ms: 1.08x slower                                      |
| 2to3                       | 267 ms                                                 | 288 ms: 1.08x slower                                       |
| pathlib                    | 17.5 ms                                                | 19.0 ms: 1.08x slower                                      |
| scimark_sor                | 124 ms                                                 | 134 ms: 1.09x slower                                       |
| chameleon                  | 6.94 ms                                                | 7.54 ms: 1.09x slower                                      |
| sqlglot_optimize           | 53.7 ms                                                | 58.5 ms: 1.09x slower                                      |
| xml_etree_iterparse        | 101 ms                                                 | 112 ms: 1.10x slower                                       |
| pyflate                    | 471 ms                                                 | 521 ms: 1.11x slower                                       |
| crypto_pyaes               | 75.3 ms                                                | 83.3 ms: 1.11x slower                                      |
| pprint_safe_repr           | 728 ms                                                 | 809 ms: 1.11x slower                                       |
| fannkuch                   | 404 ms                                                 | 450 ms: 1.11x slower                                       |
| unpickle_pure_python       | 216 us                                                 | 240 us: 1.11x slower                                       |
| tomli_loads                | 2.14 sec                                               | 2.39 sec: 1.12x slower                                     |
| pprint_pformat             | 1.49 sec                                               | 1.68 sec: 1.12x slower                                     |
| go                         | 144 ms                                                 | 163 ms: 1.13x slower                                       |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 5.74 ms: 1.14x slower                                      |
| coverage                   | 84.0 ms                                                | 95.6 ms: 1.14x slower                                      |
| raytrace                   | 267 ms                                                 | 310 ms: 1.16x slower                                       |
| float                      | 79.2 ms                                                | 92.4 ms: 1.17x slower                                      |
| regex_compile              | 132 ms                                                 | 157 ms: 1.19x slower                                       |
| scimark_fft                | 364 ms                                                 | 436 ms: 1.20x slower                                       |
| nqueens                    | 78.4 ms                                                | 94.1 ms: 1.20x slower                                      |
| scimark_monte_carlo        | 67.4 ms                                                | 81.4 ms: 1.21x slower                                      |
| spectral_norm              | 115 ms                                                 | 140 ms: 1.22x slower                                       |
| mako                       | 11.1 ms                                                | 13.7 ms: 1.24x slower                                      |
| comprehensions             | 16.5 us                                                | 20.9 us: 1.27x slower                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 731 ms: 1.27x slower                                       |
| chaos                      | 58.1 ms                                                | 74.2 ms: 1.28x slower                                      |
| python_startup_no_site     | 6.96 ms                                                | 9.00 ms: 1.29x slower                                      |
| async_tree_none            | 351 ms                                                 | 456 ms: 1.30x slower                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 611 ms: 1.32x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 583 ms: 1.32x slower                                       |
| nbody                      | 87.0 ms                                                | 119 ms: 1.36x slower                                       |
| hexiom                     | 6.16 ms                                                | 8.49 ms: 1.38x slower                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 760 ms: 1.39x slower                                       |
| async_tree_io              | 842 ms                                                 | 1.22 sec: 1.45x slower                                     |
| deltablue                  | 3.23 ms                                                | 4.67 ms: 1.45x slower                                      |
| async_tree_io_tg           | 857 ms                                                 | 1.25 sec: 1.46x slower                                     |
| async_tree_none_tg         | 321 ms                                                 | 471 ms: 1.47x slower                                       |
| Geometric mean             | (ref)                                                  | 1.09x slower                                               |

Benchmark hidden because not significant (4): asyncio_websockets, bench_mp_pool, regex_effbot, json_dumps
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, django_template, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, pylint, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (10) of results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json: asyncio_tcp, asyncio_tcp_ssl, dask, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.089x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 0.86x