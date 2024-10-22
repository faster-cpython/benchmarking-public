# Results vs. 3.13.0

- fork: mpage
- ref: gh_115999_thread_loc
- machine: linux-x86_64
- commit hash: adb59ef
- commit date: 2024-10-04
- overall geometric mean: 1.42x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x slower
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 393 ms: 1.48x slower                                                 |
| docutils       | 2.58 sec                                               | 3.24 sec: 1.25x slower                                               |
| html5lib       | 64.5 ms                                                | 93.9 ms: 1.45x slower                                                |
| tornado_http   | 91.5 ms                                                | 138 ms: 1.51x slower                                                 |
| Geometric mean | (ref)                                                  | 1.42x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 457 ms: 1.02x faster                                                 |
| async_tree_io_tg           | 825 ms                                                 | 836 ms: 1.01x slower                                                 |
| async_tree_io              | 843 ms                                                 | 897 ms: 1.06x slower                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 603 ms: 1.11x slower                                                 |
| async_tree_none_tg         | 320 ms                                                 | 356 ms: 1.11x slower                                                 |
| async_tree_none            | 354 ms                                                 | 402 ms: 1.14x slower                                                 |
| async_tree_memoization     | 442 ms                                                 | 505 ms: 1.14x slower                                                 |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 656 ms: 1.14x slower                                                 |
| asyncio_tcp                | 488 ms                                                 | 558 ms: 1.14x slower                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 2.07 sec: 1.15x slower                                               |
| async_generators           | 433 ms                                                 | 531 ms: 1.23x slower                                                 |
| coroutines                 | 22.5 ms                                                | 30.1 ms: 1.34x slower                                                |
| Geometric mean             | (ref)                                                  | 1.12x slower                                                         |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 183 ms: 1.01x faster                                                 |
| float          | 78.5 ms                                                | 137 ms: 1.75x slower                                                 |
| nbody          | 85.7 ms                                                | 189 ms: 2.20x slower                                                 |
| Geometric mean | (ref)                                                  | 1.56x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.54 ms: 1.10x faster                                                |
| regex_dna      | 220 ms                                                 | 217 ms: 1.01x faster                                                 |
| regex_v8       | 25.3 ms                                                | 25.8 ms: 1.02x slower                                                |
| regex_compile  | 131 ms                                                 | 213 ms: 1.62x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle               | 11.6 us                                                | 10.7 us: 1.08x faster                                                |
| pickle_list          | 5.01 us                                                | 4.75 us: 1.05x faster                                                |
| xml_etree_parse      | 156 ms                                                 | 150 ms: 1.04x faster                                                 |
| pickle_dict          | 33.2 us                                                | 33.0 us: 1.00x faster                                                |
| unpickle             | 14.9 us                                                | 15.9 us: 1.07x slower                                                |
| xml_etree_iterparse  | 102 ms                                                 | 112 ms: 1.10x slower                                                 |
| unpickle_list        | 4.96 us                                                | 5.49 us: 1.11x slower                                                |
| json_loads           | 27.0 us                                                | 30.3 us: 1.12x slower                                                |
| json_dumps           | 10.4 ms                                                | 12.8 ms: 1.23x slower                                                |
| xml_etree_generate   | 87.0 ms                                                | 108 ms: 1.25x slower                                                 |
| xml_etree_process    | 60.4 ms                                                | 86.8 ms: 1.44x slower                                                |
| tomli_loads          | 2.11 sec                                               | 3.17 sec: 1.50x slower                                               |
| unpickle_pure_python | 213 us                                                 | 390 us: 1.83x slower                                                 |
| pickle_pure_python   | 300 us                                                 | 564 us: 1.88x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.21x slower                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 14.3 ms: 1.35x slower                                                |
| python_startup_no_site | 6.99 ms                                                | 9.52 ms: 1.36x slower                                                |
| Geometric mean         | (ref)                                                  | 1.36x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml      | 50.3 ms                                                | 83.2 ms: 1.65x slower                                                |
| django_template | 34.4 ms                                                | 59.7 ms: 1.73x slower                                                |
| genshi_text     | 22.9 ms                                                | 39.9 ms: 1.74x slower                                                |
| mako            | 11.1 ms                                                | 20.7 ms: 1.87x slower                                                |
| Geometric mean  | (ref)                                                  | 1.75x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| gc_traversal               | 3.81 ms                                                | 2.90 ms: 1.31x faster                                                |
| create_gc_cycles           | 1.61 ms                                                | 1.39 ms: 1.15x faster                                                |
| regex_effbot               | 3.88 ms                                                | 3.54 ms: 1.10x faster                                                |
| pickle                     | 11.6 us                                                | 10.7 us: 1.08x faster                                                |
| pickle_list                | 5.01 us                                                | 4.75 us: 1.05x faster                                                |
| xml_etree_parse            | 156 ms                                                 | 150 ms: 1.04x faster                                                 |
| async_tree_memoization_tg  | 465 ms                                                 | 457 ms: 1.02x faster                                                 |
| pidigits                   | 186 ms                                                 | 183 ms: 1.01x faster                                                 |
| regex_dna                  | 220 ms                                                 | 217 ms: 1.01x faster                                                 |
| pickle_dict                | 33.2 us                                                | 33.0 us: 1.00x faster                                                |
| async_tree_io_tg           | 825 ms                                                 | 836 ms: 1.01x slower                                                 |
| regex_v8                   | 25.3 ms                                                | 25.8 ms: 1.02x slower                                                |
| async_tree_io              | 843 ms                                                 | 897 ms: 1.06x slower                                                 |
| unpickle                   | 14.9 us                                                | 15.9 us: 1.07x slower                                                |
| json                       | 5.20 ms                                                | 5.60 ms: 1.08x slower                                                |
| xml_etree_iterparse        | 102 ms                                                 | 112 ms: 1.10x slower                                                 |
| sqlite_synth               | 2.85 us                                                | 3.14 us: 1.10x slower                                                |
| unpickle_list              | 4.96 us                                                | 5.49 us: 1.11x slower                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 603 ms: 1.11x slower                                                 |
| async_tree_none_tg         | 320 ms                                                 | 356 ms: 1.11x slower                                                 |
| pathlib                    | 17.1 ms                                                | 19.1 ms: 1.12x slower                                                |
| json_loads                 | 27.0 us                                                | 30.3 us: 1.12x slower                                                |
| async_tree_none            | 354 ms                                                 | 402 ms: 1.14x slower                                                 |
| async_tree_memoization     | 442 ms                                                 | 505 ms: 1.14x slower                                                 |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 656 ms: 1.14x slower                                                 |
| asyncio_tcp                | 488 ms                                                 | 558 ms: 1.14x slower                                                 |
| scimark_fft                | 369 ms                                                 | 422 ms: 1.14x slower                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 2.07 sec: 1.15x slower                                               |
| deepcopy                   | 352 us                                                 | 408 us: 1.16x slower                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.88 ms: 1.17x slower                                                |
| telco                      | 8.45 ms                                                | 9.92 ms: 1.17x slower                                                |
| mdp                        | 2.74 sec                                               | 3.32 sec: 1.21x slower                                               |
| async_generators           | 433 ms                                                 | 531 ms: 1.23x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 12.8 ms: 1.23x slower                                                |
| xml_etree_generate         | 87.0 ms                                                | 108 ms: 1.25x slower                                                 |
| docutils                   | 2.58 sec                                               | 3.24 sec: 1.25x slower                                               |
| pylint                     | 313 ms                                                 | 394 ms: 1.26x slower                                                 |
| coverage                   | 83.7 ms                                                | 108 ms: 1.29x slower                                                 |
| meteor_contest             | 108 ms                                                 | 141 ms: 1.31x slower                                                 |
| generators                 | 28.8 ms                                                | 38.0 ms: 1.32x slower                                                |
| deepcopy_reduce            | 3.17 us                                                | 4.23 us: 1.34x slower                                                |
| coroutines                 | 22.5 ms                                                | 30.1 ms: 1.34x slower                                                |
| pycparser                  | 1.19 sec                                               | 1.60 sec: 1.34x slower                                               |
| python_startup             | 10.6 ms                                                | 14.3 ms: 1.35x slower                                                |
| bpe_tokeniser              | 4.69 sec                                               | 6.34 sec: 1.35x slower                                               |
| deepcopy_memo              | 38.0 us                                                | 51.4 us: 1.35x slower                                                |
| python_startup_no_site     | 6.99 ms                                                | 9.52 ms: 1.36x slower                                                |
| dulwich_log                | 63.0 ms                                                | 87.6 ms: 1.39x slower                                                |
| spectral_norm              | 115 ms                                                 | 163 ms: 1.42x slower                                                 |
| nqueens                    | 80.6 ms                                                | 114 ms: 1.42x slower                                                 |
| xml_etree_process          | 60.4 ms                                                | 86.8 ms: 1.44x slower                                                |
| html5lib                   | 64.5 ms                                                | 93.9 ms: 1.45x slower                                                |
| sympy_integrate            | 19.9 ms                                                | 29.4 ms: 1.48x slower                                                |
| 2to3                       | 265 ms                                                 | 393 ms: 1.48x slower                                                 |
| tomli_loads                | 2.11 sec                                               | 3.17 sec: 1.50x slower                                               |
| tornado_http               | 91.5 ms                                                | 138 ms: 1.51x slower                                                 |
| crypto_pyaes               | 73.0 ms                                                | 110 ms: 1.51x slower                                                 |
| fannkuch                   | 381 ms                                                 | 585 ms: 1.54x slower                                                 |
| thrift                     | 796 us                                                 | 1.22 ms: 1.54x slower                                                |
| typing_runtime_protocols   | 159 us                                                 | 246 us: 1.55x slower                                                 |
| sqlglot_normalize          | 107 ms                                                 | 168 ms: 1.57x slower                                                 |
| sqlglot_optimize           | 53.9 ms                                                | 84.5 ms: 1.57x slower                                                |
| sympy_str                  | 274 ms                                                 | 429 ms: 1.57x slower                                                 |
| richards                   | 48.1 ms                                                | 78.0 ms: 1.62x slower                                                |
| regex_compile              | 131 ms                                                 | 213 ms: 1.62x slower                                                 |
| pyflate                    | 460 ms                                                 | 751 ms: 1.63x slower                                                 |
| sympy_expand               | 462 ms                                                 | 758 ms: 1.64x slower                                                 |
| genshi_xml                 | 50.3 ms                                                | 83.2 ms: 1.65x slower                                                |
| pprint_safe_repr           | 744 ms                                                 | 1.25 sec: 1.69x slower                                               |
| pprint_pformat             | 1.51 sec                                               | 2.58 sec: 1.70x slower                                               |
| comprehensions             | 16.4 us                                                | 28.4 us: 1.73x slower                                                |
| django_template            | 34.4 ms                                                | 59.7 ms: 1.73x slower                                                |
| genshi_text                | 22.9 ms                                                | 39.9 ms: 1.74x slower                                                |
| float                      | 78.5 ms                                                | 137 ms: 1.75x slower                                                 |
| richards_super             | 54.4 ms                                                | 95.6 ms: 1.76x slower                                                |
| scimark_monte_carlo        | 66.3 ms                                                | 117 ms: 1.77x slower                                                 |
| sympy_sum                  | 150 ms                                                 | 265 ms: 1.77x slower                                                 |
| logging_format             | 6.25 us                                                | 11.2 us: 1.80x slower                                                |
| logging_simple             | 5.66 us                                                | 10.2 us: 1.81x slower                                                |
| unpickle_pure_python       | 213 us                                                 | 390 us: 1.83x slower                                                 |
| mako                       | 11.1 ms                                                | 20.7 ms: 1.87x slower                                                |
| pickle_pure_python         | 300 us                                                 | 564 us: 1.88x slower                                                 |
| go                         | 142 ms                                                 | 267 ms: 1.89x slower                                                 |
| chaos                      | 58.4 ms                                                | 112 ms: 1.91x slower                                                 |
| logging_silent             | 102 ns                                                 | 195 ns: 1.91x slower                                                 |
| hexiom                     | 6.13 ms                                                | 11.7 ms: 1.92x slower                                                |
| scimark_lu                 | 115 ms                                                 | 221 ms: 1.92x slower                                                 |
| sqlglot_transpile          | 1.57 ms                                                | 3.07 ms: 1.95x slower                                                |
| scimark_sor                | 122 ms                                                 | 251 ms: 2.05x slower                                                 |
| sqlglot_parse              | 1.27 ms                                                | 2.60 ms: 2.05x slower                                                |
| raytrace                   | 262 ms                                                 | 564 ms: 2.16x slower                                                 |
| nbody                      | 85.7 ms                                                | 189 ms: 2.20x slower                                                 |
| deltablue                  | 3.15 ms                                                | 8.21 ms: 2.61x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 66.3 ms: 2.76x slower                                                |
| unpack_sequence            | 42.4 ns                                                | 150 ns: 3.55x slower                                                 |
| bench_thread_pool          | 815 us                                                 | 3.44 ms: 4.22x slower                                                |
| Geometric mean             | (ref)                                                  | 1.42x slower                                                         |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.34x
- 95% likely to have a slowdown of 1.31x
- 99% likely to have a slowdown of 1.27x

# Memory
- memory change: 1.18x