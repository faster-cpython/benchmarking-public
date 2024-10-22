# Results vs. 3.13.0

- fork: brandtbucher
- ref: underflow_cache_dyna
- machine: linux-x86_64
- commit hash: 7e695c6
- commit date: 2024-08-29
- overall geometric mean: 1.01x slower
- HPT reliability: 71.64%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 282 ms: 1.07x slower                                                        |
| docutils       | 2.58 sec                                               | 3.30 sec: 1.28x slower                                                      |
| html5lib       | 64.5 ms                                                | 76.2 ms: 1.18x slower                                                       |
| tornado_http   | 91.5 ms                                                | 99.5 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                  | 1.15x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 410 ms: 1.13x faster                                                        |
| async_tree_none           | 354 ms                                                 | 328 ms: 1.08x faster                                                        |
| async_tree_memoization    | 442 ms                                                 | 411 ms: 1.08x faster                                                        |
| async_tree_none_tg        | 320 ms                                                 | 314 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 565 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                      |
| asyncio_tcp               | 488 ms                                                 | 503 ms: 1.03x slower                                                        |
| coroutines                | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                       |
| async_generators          | 433 ms                                                 | 465 ms: 1.08x slower                                                        |
| async_tree_io_tg          | 825 ms                                                 | 901 ms: 1.09x slower                                                        |
| async_tree_io             | 843 ms                                                 | 936 ms: 1.11x slower                                                        |
| Geometric mean            | (ref)                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 71.1 ms: 1.10x faster                                                       |
| nbody          | 85.7 ms                                                | 79.3 ms: 1.08x faster                                                       |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                | 24.4 ms: 1.03x faster                                                       |
| regex_effbot   | 3.88 ms                                                | 3.76 ms: 1.03x faster                                                       |
| regex_dna      | 220 ms                                                 | 221 ms: 1.01x slower                                                        |
| regex_compile  | 131 ms                                                 | 154 ms: 1.18x slower                                                        |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 77.1 ms: 1.13x faster                                                       |
| xml_etree_process    | 60.4 ms                                                | 54.8 ms: 1.10x faster                                                       |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                        |
| tomli_loads          | 2.11 sec                                               | 1.99 sec: 1.06x faster                                                      |
| unpickle_pure_python | 213 us                                                 | 203 us: 1.05x faster                                                        |
| json_dumps           | 10.4 ms                                                | 9.94 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 102 ms                                                 | 98.5 ms: 1.04x faster                                                       |
| pickle_pure_python   | 300 us                                                 | 310 us: 1.03x slower                                                        |
| json_loads           | 27.0 us                                                | 29.5 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                | 7.17 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.74 ms: 1.14x faster                                                       |
| django_template | 34.4 ms                                                | 38.9 ms: 1.13x slower                                                       |
| genshi_xml      | 50.3 ms                                                | 64.0 ms: 1.27x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                                |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 26.1 us: 1.46x faster                                                       |
| deepcopy                  | 352 us                                                 | 267 us: 1.32x faster                                                        |
| richards                  | 48.1 ms                                                | 40.4 ms: 1.19x faster                                                       |
| richards_super            | 54.4 ms                                                | 45.8 ms: 1.19x faster                                                       |
| deepcopy_reduce           | 3.17 us                                                | 2.68 us: 1.18x faster                                                       |
| scimark_fft               | 369 ms                                                 | 315 ms: 1.17x faster                                                        |
| spectral_norm             | 115 ms                                                 | 101 ms: 1.14x faster                                                        |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.40 ms: 1.14x faster                                                       |
| scimark_lu                | 115 ms                                                 | 101 ms: 1.14x faster                                                        |
| mako                      | 11.1 ms                                                | 9.74 ms: 1.14x faster                                                       |
| async_tree_memoization_tg | 465 ms                                                 | 410 ms: 1.13x faster                                                        |
| xml_etree_generate        | 87.0 ms                                                | 77.1 ms: 1.13x faster                                                       |
| float                     | 78.5 ms                                                | 71.1 ms: 1.10x faster                                                       |
| xml_etree_process         | 60.4 ms                                                | 54.8 ms: 1.10x faster                                                       |
| telco                     | 8.45 ms                                                | 7.69 ms: 1.10x faster                                                       |
| nbody                     | 85.7 ms                                                | 79.3 ms: 1.08x faster                                                       |
| crypto_pyaes              | 73.0 ms                                                | 67.5 ms: 1.08x faster                                                       |
| mdp                       | 2.74 sec                                               | 2.54 sec: 1.08x faster                                                      |
| async_tree_none           | 354 ms                                                 | 328 ms: 1.08x faster                                                        |
| logging_silent            | 102 ns                                                 | 94.7 ns: 1.08x faster                                                       |
| async_tree_memoization    | 442 ms                                                 | 411 ms: 1.08x faster                                                        |
| scimark_monte_carlo       | 66.3 ms                                                | 61.7 ms: 1.07x faster                                                       |
| pathlib                   | 17.1 ms                                                | 15.9 ms: 1.07x faster                                                       |
| xml_etree_parse           | 156 ms                                                 | 146 ms: 1.07x faster                                                        |
| tomli_loads               | 2.11 sec                                               | 1.99 sec: 1.06x faster                                                      |
| bpe_tokeniser             | 4.69 sec                                               | 4.44 sec: 1.06x faster                                                      |
| unpickle_pure_python      | 213 us                                                 | 203 us: 1.05x faster                                                        |
| json_dumps                | 10.4 ms                                                | 9.94 ms: 1.05x faster                                                       |
| xml_etree_iterparse       | 102 ms                                                 | 98.5 ms: 1.04x faster                                                       |
| regex_v8                  | 25.3 ms                                                | 24.4 ms: 1.03x faster                                                       |
| regex_effbot              | 3.88 ms                                                | 3.76 ms: 1.03x faster                                                       |
| pprint_safe_repr          | 744 ms                                                 | 723 ms: 1.03x faster                                                        |
| pprint_pformat            | 1.51 sec                                               | 1.48 sec: 1.02x faster                                                      |
| async_tree_none_tg        | 320 ms                                                 | 314 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 565 ms: 1.02x faster                                                        |
| pyflate                   | 460 ms                                                 | 454 ms: 1.01x faster                                                        |
| gc_traversal              | 3.81 ms                                                | 3.78 ms: 1.01x faster                                                       |
| meteor_contest            | 108 ms                                                 | 107 ms: 1.01x faster                                                        |
| pidigits                  | 186 ms                                                 | 187 ms: 1.01x slower                                                        |
| regex_dna                 | 220 ms                                                 | 221 ms: 1.01x slower                                                        |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                      |
| logging_simple            | 5.66 us                                                | 5.73 us: 1.01x slower                                                       |
| comprehensions            | 16.4 us                                                | 16.6 us: 1.01x slower                                                       |
| json                      | 5.20 ms                                                | 5.28 ms: 1.02x slower                                                       |
| bench_thread_pool         | 815 us                                                 | 830 us: 1.02x slower                                                        |
| chaos                     | 58.4 ms                                                | 59.6 ms: 1.02x slower                                                       |
| python_startup_no_site    | 6.99 ms                                                | 7.17 ms: 1.03x slower                                                       |
| typing_runtime_protocols  | 159 us                                                 | 164 us: 1.03x slower                                                        |
| asyncio_tcp               | 488 ms                                                 | 503 ms: 1.03x slower                                                        |
| coroutines                | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                       |
| pickle_pure_python        | 300 us                                                 | 310 us: 1.03x slower                                                        |
| nqueens                   | 80.6 ms                                                | 83.8 ms: 1.04x slower                                                       |
| deltablue                 | 3.15 ms                                                | 3.27 ms: 1.04x slower                                                       |
| coverage                  | 83.7 ms                                                | 87.4 ms: 1.04x slower                                                       |
| 2to3                      | 265 ms                                                 | 282 ms: 1.07x slower                                                        |
| async_generators          | 433 ms                                                 | 465 ms: 1.08x slower                                                        |
| raytrace                  | 262 ms                                                 | 282 ms: 1.08x slower                                                        |
| tornado_http              | 91.5 ms                                                | 99.5 ms: 1.09x slower                                                       |
| async_tree_io_tg          | 825 ms                                                 | 901 ms: 1.09x slower                                                        |
| json_loads                | 27.0 us                                                | 29.5 us: 1.10x slower                                                       |
| create_gc_cycles          | 1.61 ms                                                | 1.78 ms: 1.11x slower                                                       |
| sqlglot_optimize          | 53.9 ms                                                | 59.7 ms: 1.11x slower                                                       |
| async_tree_io             | 843 ms                                                 | 936 ms: 1.11x slower                                                        |
| sqlglot_normalize         | 107 ms                                                 | 120 ms: 1.12x slower                                                        |
| django_template           | 34.4 ms                                                | 38.9 ms: 1.13x slower                                                       |
| sympy_expand              | 462 ms                                                 | 528 ms: 1.14x slower                                                        |
| sqlglot_transpile         | 1.57 ms                                                | 1.80 ms: 1.14x slower                                                       |
| hexiom                    | 6.13 ms                                                | 7.04 ms: 1.15x slower                                                       |
| sympy_str                 | 274 ms                                                 | 321 ms: 1.17x slower                                                        |
| regex_compile             | 131 ms                                                 | 154 ms: 1.18x slower                                                        |
| html5lib                  | 64.5 ms                                                | 76.2 ms: 1.18x slower                                                       |
| pycparser                 | 1.19 sec                                               | 1.42 sec: 1.19x slower                                                      |
| generators                | 28.8 ms                                                | 34.3 ms: 1.19x slower                                                       |
| sympy_integrate           | 19.9 ms                                                | 23.7 ms: 1.19x slower                                                       |
| sympy_sum                 | 150 ms                                                 | 180 ms: 1.20x slower                                                        |
| sqlglot_parse             | 1.27 ms                                                | 1.53 ms: 1.21x slower                                                       |
| go                        | 142 ms                                                 | 173 ms: 1.22x slower                                                        |
| scimark_sor               | 122 ms                                                 | 154 ms: 1.26x slower                                                        |
| genshi_xml                | 50.3 ms                                                | 64.0 ms: 1.27x slower                                                       |
| docutils                  | 2.58 sec                                               | 3.30 sec: 1.28x slower                                                      |
| pylint                    | 313 ms                                                 | 406 ms: 1.30x slower                                                        |
| Geometric mean            | (ref)                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (8): fannkuch, thrift, python_startup, bench_mp_pool, asyncio_websockets, logging_format, genshi_text, async_tree_cpu_io_mixed_tg
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 71.64% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.11x