# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a3
- machine: linux-x86_64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.084x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: 0.87x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 282 ms: 1.06x slower                                       |
| chameleon      | 6.94 ms                                                | 7.24 ms: 1.04x slower                                      |
| docutils       | 2.59 sec                                               | 2.71 sec: 1.05x slower                                     |
| tornado_http   | 92.4 ms                                                | 97.8 ms: 1.06x slower                                      |
| Geometric mean | (ref)                                                  | 1.05x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_generators           | 436 ms                                                 | 461 ms: 1.06x slower                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 718 ms: 1.24x slower                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 587 ms: 1.27x slower                                       |
| async_tree_none            | 351 ms                                                 | 448 ms: 1.28x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 574 ms: 1.30x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 727 ms: 1.33x slower                                       |
| async_tree_none_tg         | 321 ms                                                 | 449 ms: 1.40x slower                                       |
| async_tree_io_tg           | 857 ms                                                 | 1.21 sec: 1.41x slower                                     |
| async_tree_io              | 842 ms                                                 | 1.20 sec: 1.43x slower                                     |
| Geometric mean             | (ref)                                                  | 1.24x slower                                               |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 190 ms: 1.02x slower                                       |
| float          | 79.2 ms                                                | 94.1 ms: 1.19x slower                                      |
| nbody          | 87.0 ms                                                | 119 ms: 1.37x slower                                       |
| Geometric mean | (ref)                                                  | 1.18x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.6 ms: 1.07x faster                                      |
| regex_effbot   | 3.73 ms                                                | 3.74 ms: 1.00x slower                                      |
| regex_dna      | 218 ms                                                 | 228 ms: 1.04x slower                                       |
| regex_compile  | 132 ms                                                 | 153 ms: 1.16x slower                                       |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 310 us                                                 | 301 us: 1.03x faster                                       |
| json_dumps           | 10.6 ms                                                | 10.5 ms: 1.01x faster                                      |
| xml_etree_process    | 60.6 ms                                                | 61.1 ms: 1.01x slower                                      |
| xml_etree_parse      | 156 ms                                                 | 159 ms: 1.02x slower                                       |
| xml_etree_generate   | 86.7 ms                                                | 89.5 ms: 1.03x slower                                      |
| json_loads           | 27.2 us                                                | 28.2 us: 1.03x slower                                      |
| unpickle_pure_python | 216 us                                                 | 234 us: 1.08x slower                                       |
| xml_etree_iterparse  | 101 ms                                                 | 112 ms: 1.11x slower                                       |
| tomli_loads          | 2.14 sec                                               | 2.61 sec: 1.22x slower                                     |
| Geometric mean       | (ref)                                                  | 1.05x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.1 ms: 1.24x faster                                      |
| python_startup_no_site | 6.96 ms                                                | 8.72 ms: 1.25x slower                                      |
| Geometric mean         | (ref)                                                  | 1.01x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 11.1 ms                                                | 14.2 ms: 1.28x slower                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles           | 2.41 ms                                                | 1.49 ms: 1.62x faster                                      |
| typing_runtime_protocols   | 165 us                                                 | 117 us: 1.41x faster                                       |
| python_startup             | 12.5 ms                                                | 10.1 ms: 1.24x faster                                      |
| mypy2                      | 1.04 sec                                               | 865 ms: 1.21x faster                                       |
| gc_traversal               | 4.37 ms                                                | 3.69 ms: 1.18x faster                                      |
| regex_v8                   | 26.2 ms                                                | 24.6 ms: 1.07x faster                                      |
| json                       | 5.36 ms                                                | 5.19 ms: 1.03x faster                                      |
| pickle_pure_python         | 310 us                                                 | 301 us: 1.03x faster                                       |
| mdp                        | 2.72 sec                                               | 2.67 sec: 1.02x faster                                     |
| deepcopy_reduce            | 3.20 us                                                | 3.15 us: 1.02x faster                                      |
| richards                   | 48.7 ms                                                | 48.3 ms: 1.01x faster                                      |
| pycparser                  | 1.20 sec                                               | 1.19 sec: 1.01x faster                                     |
| json_dumps                 | 10.6 ms                                                | 10.5 ms: 1.01x faster                                      |
| regex_effbot               | 3.73 ms                                                | 3.74 ms: 1.00x slower                                      |
| logging_silent             | 102 ns                                                 | 102 ns: 1.00x slower                                       |
| xml_etree_process          | 60.6 ms                                                | 61.1 ms: 1.01x slower                                      |
| telco                      | 8.54 ms                                                | 8.62 ms: 1.01x slower                                      |
| generators                 | 29.0 ms                                                | 29.3 ms: 1.01x slower                                      |
| pidigits                   | 186 ms                                                 | 190 ms: 1.02x slower                                       |
| xml_etree_parse            | 156 ms                                                 | 159 ms: 1.02x slower                                       |
| xml_etree_generate         | 86.7 ms                                                | 89.5 ms: 1.03x slower                                      |
| bench_thread_pool          | 822 us                                                 | 848 us: 1.03x slower                                       |
| json_loads                 | 27.2 us                                                | 28.2 us: 1.03x slower                                      |
| pathlib                    | 17.5 ms                                                | 18.3 ms: 1.04x slower                                      |
| regex_dna                  | 218 ms                                                 | 228 ms: 1.04x slower                                       |
| deepcopy_memo              | 39.1 us                                                | 40.8 us: 1.04x slower                                      |
| chameleon                  | 6.94 ms                                                | 7.24 ms: 1.04x slower                                      |
| meteor_contest             | 109 ms                                                 | 114 ms: 1.04x slower                                       |
| docutils                   | 2.59 sec                                               | 2.71 sec: 1.05x slower                                     |
| sqlglot_parse              | 1.27 ms                                                | 1.34 ms: 1.05x slower                                      |
| 2to3                       | 267 ms                                                 | 282 ms: 1.06x slower                                       |
| sqlglot_transpile          | 1.58 ms                                                | 1.67 ms: 1.06x slower                                      |
| async_generators           | 436 ms                                                 | 461 ms: 1.06x slower                                       |
| tornado_http               | 92.4 ms                                                | 97.8 ms: 1.06x slower                                      |
| scimark_lu                 | 113 ms                                                 | 119 ms: 1.06x slower                                       |
| sympy_integrate            | 19.9 ms                                                | 21.1 ms: 1.06x slower                                      |
| sympy_expand               | 463 ms                                                 | 495 ms: 1.07x slower                                       |
| dulwich_log                | 64.3 ms                                                | 69.0 ms: 1.07x slower                                      |
| sympy_sum                  | 150 ms                                                 | 161 ms: 1.07x slower                                       |
| sqlglot_normalize          | 108 ms                                                 | 116 ms: 1.08x slower                                       |
| scimark_sor                | 124 ms                                                 | 134 ms: 1.08x slower                                       |
| logging_simple             | 5.72 us                                                | 6.20 us: 1.08x slower                                      |
| unpickle_pure_python       | 216 us                                                 | 234 us: 1.08x slower                                       |
| go                         | 144 ms                                                 | 156 ms: 1.08x slower                                       |
| sqlglot_optimize           | 53.7 ms                                                | 58.4 ms: 1.09x slower                                      |
| sympy_str                  | 275 ms                                                 | 302 ms: 1.10x slower                                       |
| logging_format             | 6.40 us                                                | 7.07 us: 1.10x slower                                      |
| xml_etree_iterparse        | 101 ms                                                 | 112 ms: 1.11x slower                                       |
| pprint_safe_repr           | 728 ms                                                 | 816 ms: 1.12x slower                                       |
| fannkuch                   | 404 ms                                                 | 454 ms: 1.12x slower                                       |
| crypto_pyaes               | 75.3 ms                                                | 85.0 ms: 1.13x slower                                      |
| raytrace                   | 267 ms                                                 | 302 ms: 1.13x slower                                       |
| coverage                   | 84.0 ms                                                | 95.0 ms: 1.13x slower                                      |
| pprint_pformat             | 1.49 sec                                               | 1.70 sec: 1.14x slower                                     |
| pyflate                    | 471 ms                                                 | 536 ms: 1.14x slower                                       |
| regex_compile              | 132 ms                                                 | 153 ms: 1.16x slower                                       |
| float                      | 79.2 ms                                                | 94.1 ms: 1.19x slower                                      |
| scimark_monte_carlo        | 67.4 ms                                                | 81.4 ms: 1.21x slower                                      |
| nqueens                    | 78.4 ms                                                | 95.4 ms: 1.22x slower                                      |
| tomli_loads                | 2.14 sec                                               | 2.61 sec: 1.22x slower                                     |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 718 ms: 1.24x slower                                       |
| python_startup_no_site     | 6.96 ms                                                | 8.72 ms: 1.25x slower                                      |
| scimark_fft                | 364 ms                                                 | 457 ms: 1.26x slower                                       |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 6.38 ms: 1.26x slower                                      |
| async_tree_memoization_tg  | 464 ms                                                 | 587 ms: 1.27x slower                                       |
| chaos                      | 58.1 ms                                                | 73.6 ms: 1.27x slower                                      |
| async_tree_none            | 351 ms                                                 | 448 ms: 1.28x slower                                       |
| mako                       | 11.1 ms                                                | 14.2 ms: 1.28x slower                                      |
| async_tree_memoization     | 442 ms                                                 | 574 ms: 1.30x slower                                       |
| comprehensions             | 16.5 us                                                | 21.6 us: 1.31x slower                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 727 ms: 1.33x slower                                       |
| spectral_norm              | 115 ms                                                 | 154 ms: 1.34x slower                                       |
| nbody                      | 87.0 ms                                                | 119 ms: 1.37x slower                                       |
| async_tree_none_tg         | 321 ms                                                 | 449 ms: 1.40x slower                                       |
| hexiom                     | 6.16 ms                                                | 8.65 ms: 1.40x slower                                      |
| async_tree_io_tg           | 857 ms                                                 | 1.21 sec: 1.41x slower                                     |
| async_tree_io              | 842 ms                                                 | 1.20 sec: 1.43x slower                                     |
| deltablue                  | 3.23 ms                                                | 4.85 ms: 1.50x slower                                      |
| Geometric mean             | (ref)                                                  | 1.09x slower                                               |

Benchmark hidden because not significant (5): richards_super, coroutines, asyncio_websockets, bench_mp_pool, deepcopy
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, django_template, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, pylint, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (10) of results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json: asyncio_tcp, asyncio_tcp_ssl, dask, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.084x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 0.87x