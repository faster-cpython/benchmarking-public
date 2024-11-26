# Results vs. 3.13.0

- fork: mpage
- ref: gh_115999_thread_loc
- machine: linux-x86_64
- commit hash: adb59ef
- commit date: 2024-10-04
- overall geometric mean: 1.281x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 393 ms: 1.47x slower                                                 |
| docutils       | 2.59 sec                                               | 3.24 sec: 1.25x slower                                               |
| html5lib       | 64.2 ms                                                | 93.9 ms: 1.46x slower                                                |
| tornado_http   | 92.4 ms                                                | 138 ms: 1.49x slower                                                 |
| Geometric mean | (ref)                                                  | 1.42x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 857 ms                                                 | 836 ms: 1.02x faster                                                 |
| async_tree_memoization_tg  | 464 ms                                                 | 457 ms: 1.01x faster                                                 |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                                 |
| async_tree_io              | 842 ms                                                 | 897 ms: 1.07x slower                                                 |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 603 ms: 1.10x slower                                                 |
| async_tree_none_tg         | 321 ms                                                 | 356 ms: 1.11x slower                                                 |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 656 ms: 1.14x slower                                                 |
| async_tree_memoization     | 442 ms                                                 | 505 ms: 1.14x slower                                                 |
| async_tree_none            | 351 ms                                                 | 402 ms: 1.15x slower                                                 |
| async_generators           | 436 ms                                                 | 531 ms: 1.22x slower                                                 |
| coroutines                 | 22.7 ms                                                | 30.1 ms: 1.33x slower                                                |
| Geometric mean             | (ref)                                                  | 1.11x slower                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 183 ms: 1.02x faster                                                 |
| float          | 79.2 ms                                                | 137 ms: 1.73x slower                                                 |
| nbody          | 87.0 ms                                                | 189 ms: 2.17x slower                                                 |
| Geometric mean | (ref)                                                  | 1.55x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.54 ms: 1.05x faster                                                |
| regex_v8       | 26.2 ms                                                | 25.8 ms: 1.02x faster                                                |
| regex_dna      | 218 ms                                                 | 217 ms: 1.01x faster                                                 |
| regex_compile  | 132 ms                                                 | 213 ms: 1.61x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_parse      | 156 ms                                                 | 150 ms: 1.04x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 112 ms: 1.11x slower                                                 |
| json_loads           | 27.2 us                                                | 30.3 us: 1.11x slower                                                |
| json_dumps           | 10.6 ms                                                | 12.8 ms: 1.22x slower                                                |
| xml_etree_generate   | 86.7 ms                                                | 108 ms: 1.25x slower                                                 |
| xml_etree_process    | 60.6 ms                                                | 86.8 ms: 1.43x slower                                                |
| tomli_loads          | 2.14 sec                                               | 3.17 sec: 1.48x slower                                               |
| unpickle_pure_python | 216 us                                                 | 390 us: 1.81x slower                                                 |
| pickle_pure_python   | 310 us                                                 | 564 us: 1.82x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.32x slower                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 14.3 ms: 1.14x slower                                                |
| python_startup_no_site | 6.96 ms                                                | 9.52 ms: 1.37x slower                                                |
| Geometric mean         | (ref)                                                  | 1.25x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml      | 50.9 ms                                                | 83.2 ms: 1.63x slower                                                |
| genshi_text     | 23.5 ms                                                | 39.9 ms: 1.69x slower                                                |
| django_template | 35.2 ms                                                | 59.7 ms: 1.70x slower                                                |
| mako            | 11.1 ms                                                | 20.7 ms: 1.87x slower                                                |
| Geometric mean  | (ref)                                                  | 1.72x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| create_gc_cycles           | 2.41 ms                                                | 1.39 ms: 1.73x faster                                                |
| gc_traversal               | 4.37 ms                                                | 2.90 ms: 1.51x faster                                                |
| regex_effbot               | 3.73 ms                                                | 3.54 ms: 1.05x faster                                                |
| xml_etree_parse            | 156 ms                                                 | 150 ms: 1.04x faster                                                 |
| async_tree_io_tg           | 857 ms                                                 | 836 ms: 1.02x faster                                                 |
| regex_v8                   | 26.2 ms                                                | 25.8 ms: 1.02x faster                                                |
| pidigits                   | 186 ms                                                 | 183 ms: 1.02x faster                                                 |
| async_tree_memoization_tg  | 464 ms                                                 | 457 ms: 1.01x faster                                                 |
| regex_dna                  | 218 ms                                                 | 217 ms: 1.01x faster                                                 |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                                 |
| json                       | 5.36 ms                                                | 5.60 ms: 1.04x slower                                                |
| async_tree_io              | 842 ms                                                 | 897 ms: 1.07x slower                                                 |
| pathlib                    | 17.5 ms                                                | 19.1 ms: 1.09x slower                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 603 ms: 1.10x slower                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 112 ms: 1.11x slower                                                 |
| async_tree_none_tg         | 321 ms                                                 | 356 ms: 1.11x slower                                                 |
| json_loads                 | 27.2 us                                                | 30.3 us: 1.11x slower                                                |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 656 ms: 1.14x slower                                                 |
| deepcopy                   | 358 us                                                 | 408 us: 1.14x slower                                                 |
| async_tree_memoization     | 442 ms                                                 | 505 ms: 1.14x slower                                                 |
| python_startup             | 12.5 ms                                                | 14.3 ms: 1.14x slower                                                |
| async_tree_none            | 351 ms                                                 | 402 ms: 1.15x slower                                                 |
| scimark_fft                | 364 ms                                                 | 422 ms: 1.16x slower                                                 |
| telco                      | 8.54 ms                                                | 9.92 ms: 1.16x slower                                                |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 5.88 ms: 1.17x slower                                                |
| json_dumps                 | 10.6 ms                                                | 12.8 ms: 1.22x slower                                                |
| async_generators           | 436 ms                                                 | 531 ms: 1.22x slower                                                 |
| mdp                        | 2.72 sec                                               | 3.32 sec: 1.22x slower                                               |
| docutils                   | 2.59 sec                                               | 3.24 sec: 1.25x slower                                               |
| xml_etree_generate         | 86.7 ms                                                | 108 ms: 1.25x slower                                                 |
| pylint                     | 313 ms                                                 | 394 ms: 1.26x slower                                                 |
| coverage                   | 84.0 ms                                                | 108 ms: 1.29x slower                                                 |
| meteor_contest             | 109 ms                                                 | 141 ms: 1.29x slower                                                 |
| generators                 | 29.0 ms                                                | 38.0 ms: 1.31x slower                                                |
| deepcopy_memo              | 39.1 us                                                | 51.4 us: 1.32x slower                                                |
| deepcopy_reduce            | 3.20 us                                                | 4.23 us: 1.32x slower                                                |
| coroutines                 | 22.7 ms                                                | 30.1 ms: 1.33x slower                                                |
| pycparser                  | 1.20 sec                                               | 1.60 sec: 1.33x slower                                               |
| bpe_tokeniser              | 4.75 sec                                               | 6.34 sec: 1.34x slower                                               |
| dulwich_log                | 64.3 ms                                                | 87.6 ms: 1.36x slower                                                |
| python_startup_no_site     | 6.96 ms                                                | 9.52 ms: 1.37x slower                                                |
| spectral_norm              | 115 ms                                                 | 163 ms: 1.41x slower                                                 |
| xml_etree_process          | 60.6 ms                                                | 86.8 ms: 1.43x slower                                                |
| fannkuch                   | 404 ms                                                 | 585 ms: 1.45x slower                                                 |
| nqueens                    | 78.4 ms                                                | 114 ms: 1.46x slower                                                 |
| html5lib                   | 64.2 ms                                                | 93.9 ms: 1.46x slower                                                |
| crypto_pyaes               | 75.3 ms                                                | 110 ms: 1.46x slower                                                 |
| 2to3                       | 267 ms                                                 | 393 ms: 1.47x slower                                                 |
| sympy_integrate            | 19.9 ms                                                | 29.4 ms: 1.48x slower                                                |
| tomli_loads                | 2.14 sec                                               | 3.17 sec: 1.48x slower                                               |
| typing_runtime_protocols   | 165 us                                                 | 246 us: 1.49x slower                                                 |
| tornado_http               | 92.4 ms                                                | 138 ms: 1.49x slower                                                 |
| thrift                     | 809 us                                                 | 1.22 ms: 1.51x slower                                                |
| sympy_str                  | 275 ms                                                 | 429 ms: 1.56x slower                                                 |
| sqlglot_normalize          | 108 ms                                                 | 168 ms: 1.56x slower                                                 |
| sqlglot_optimize           | 53.7 ms                                                | 84.5 ms: 1.57x slower                                                |
| pyflate                    | 471 ms                                                 | 751 ms: 1.59x slower                                                 |
| richards                   | 48.7 ms                                                | 78.0 ms: 1.60x slower                                                |
| regex_compile              | 132 ms                                                 | 213 ms: 1.61x slower                                                 |
| genshi_xml                 | 50.9 ms                                                | 83.2 ms: 1.63x slower                                                |
| sympy_expand               | 463 ms                                                 | 758 ms: 1.64x slower                                                 |
| genshi_text                | 23.5 ms                                                | 39.9 ms: 1.69x slower                                                |
| django_template            | 35.2 ms                                                | 59.7 ms: 1.70x slower                                                |
| comprehensions             | 16.5 us                                                | 28.4 us: 1.72x slower                                                |
| pprint_safe_repr           | 728 ms                                                 | 1.25 sec: 1.72x slower                                               |
| pprint_pformat             | 1.49 sec                                               | 2.58 sec: 1.72x slower                                               |
| float                      | 79.2 ms                                                | 137 ms: 1.73x slower                                                 |
| scimark_monte_carlo        | 67.4 ms                                                | 117 ms: 1.74x slower                                                 |
| richards_super             | 54.9 ms                                                | 95.6 ms: 1.74x slower                                                |
| logging_format             | 6.40 us                                                | 11.2 us: 1.76x slower                                                |
| sympy_sum                  | 150 ms                                                 | 265 ms: 1.76x slower                                                 |
| logging_simple             | 5.72 us                                                | 10.2 us: 1.79x slower                                                |
| unpickle_pure_python       | 216 us                                                 | 390 us: 1.81x slower                                                 |
| pickle_pure_python         | 310 us                                                 | 564 us: 1.82x slower                                                 |
| go                         | 144 ms                                                 | 267 ms: 1.86x slower                                                 |
| mako                       | 11.1 ms                                                | 20.7 ms: 1.87x slower                                                |
| hexiom                     | 6.16 ms                                                | 11.7 ms: 1.91x slower                                                |
| logging_silent             | 102 ns                                                 | 195 ns: 1.92x slower                                                 |
| chaos                      | 58.1 ms                                                | 112 ms: 1.93x slower                                                 |
| sqlglot_transpile          | 1.58 ms                                                | 3.07 ms: 1.94x slower                                                |
| scimark_lu                 | 113 ms                                                 | 221 ms: 1.96x slower                                                 |
| scimark_sor                | 124 ms                                                 | 251 ms: 2.03x slower                                                 |
| sqlglot_parse              | 1.27 ms                                                | 2.60 ms: 2.04x slower                                                |
| raytrace                   | 267 ms                                                 | 564 ms: 2.11x slower                                                 |
| nbody                      | 87.0 ms                                                | 189 ms: 2.17x slower                                                 |
| deltablue                  | 3.23 ms                                                | 8.21 ms: 2.54x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 66.3 ms: 2.76x slower                                                |
| bench_thread_pool          | 822 us                                                 | 3.44 ms: 4.19x slower                                                |
| Geometric mean             | (ref)                                                  | 1.42x slower                                                         |
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241004-3.14.0a0-adb59ef-NOGIL/bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.281x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.32x
- 95% likely to have a slowdown of 1.30x
- 99% likely to have a slowdown of 1.26x

# Memory
- memory change: 1.07x