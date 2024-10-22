# Results vs. 3.13.0

- fork: brandtbucher
- ref: underflow_jump_backw
- machine: linux-x86_64
- commit hash: e448061
- commit date: 2024-08-29
- overall geometric mean: 1.05x slower
- HPT reliability: 99.48%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 290 ms: 1.09x slower                                                        |
| docutils       | 2.58 sec                                               | 3.58 sec: 1.38x slower                                                      |
| html5lib       | 64.5 ms                                                | 75.5 ms: 1.17x slower                                                       |
| tornado_http   | 91.5 ms                                                | 120 ms: 1.31x slower                                                        |
| Geometric mean | (ref)                                                  | 1.23x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 416 ms: 1.12x faster                                                        |
| async_tree_none            | 354 ms                                                 | 347 ms: 1.02x faster                                                        |
| asyncio_websockets         | 555 ms                                                 | 559 ms: 1.01x slower                                                        |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 581 ms: 1.01x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.83 sec: 1.02x slower                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 558 ms: 1.03x slower                                                        |
| async_generators           | 433 ms                                                 | 457 ms: 1.05x slower                                                        |
| coroutines                 | 22.5 ms                                                | 24.0 ms: 1.07x slower                                                       |
| async_tree_io_tg           | 825 ms                                                 | 896 ms: 1.09x slower                                                        |
| asyncio_tcp                | 488 ms                                                 | 531 ms: 1.09x slower                                                        |
| async_tree_io              | 843 ms                                                 | 966 ms: 1.15x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.03x slower                                                                |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.4 ms: 1.11x faster                                                       |
| nbody          | 85.7 ms                                                | 80.3 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.79 ms: 1.03x faster                                                       |
| regex_dna      | 220 ms                                                 | 221 ms: 1.00x slower                                                        |
| regex_v8       | 25.3 ms                                                | 25.5 ms: 1.01x slower                                                       |
| regex_compile  | 131 ms                                                 | 147 ms: 1.12x slower                                                        |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 81.4 ms: 1.07x faster                                                       |
| xml_etree_parse      | 156 ms                                                 | 147 ms: 1.06x faster                                                        |
| xml_etree_process    | 60.4 ms                                                | 57.2 ms: 1.06x faster                                                       |
| json_dumps           | 10.4 ms                                                | 9.97 ms: 1.04x faster                                                       |
| pickle_pure_python   | 300 us                                                 | 288 us: 1.04x faster                                                        |
| xml_etree_iterparse  | 102 ms                                                 | 98.2 ms: 1.04x faster                                                       |
| unpickle_pure_python | 213 us                                                 | 211 us: 1.01x faster                                                        |
| tomli_loads          | 2.11 sec                                               | 2.18 sec: 1.03x slower                                                      |
| json_loads           | 27.0 us                                                | 28.3 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.01x slower                                                       |
| python_startup_no_site | 6.99 ms                                                | 7.19 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.3 ms: 1.07x faster                                                       |
| genshi_text     | 22.9 ms                                                | 24.3 ms: 1.06x slower                                                       |
| django_template | 34.4 ms                                                | 42.1 ms: 1.22x slower                                                       |
| genshi_xml      | 50.3 ms                                                | 67.5 ms: 1.34x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.13x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 28.9 us: 1.31x faster                                                       |
| deepcopy                   | 352 us                                                 | 272 us: 1.30x faster                                                        |
| scimark_fft                | 369 ms                                                 | 301 ms: 1.22x faster                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.34 ms: 1.16x faster                                                       |
| scimark_monte_carlo        | 66.3 ms                                                | 58.9 ms: 1.13x faster                                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 416 ms: 1.12x faster                                                        |
| float                      | 78.5 ms                                                | 70.4 ms: 1.11x faster                                                       |
| crypto_pyaes               | 73.0 ms                                                | 65.7 ms: 1.11x faster                                                       |
| deepcopy_reduce            | 3.17 us                                                | 2.86 us: 1.11x faster                                                       |
| telco                      | 8.45 ms                                                | 7.64 ms: 1.11x faster                                                       |
| pathlib                    | 17.1 ms                                                | 15.7 ms: 1.09x faster                                                       |
| pprint_safe_repr           | 744 ms                                                 | 688 ms: 1.08x faster                                                        |
| mako                       | 11.1 ms                                                | 10.3 ms: 1.07x faster                                                       |
| spectral_norm              | 115 ms                                                 | 107 ms: 1.07x faster                                                        |
| xml_etree_generate         | 87.0 ms                                                | 81.4 ms: 1.07x faster                                                       |
| nbody                      | 85.7 ms                                                | 80.3 ms: 1.07x faster                                                       |
| xml_etree_parse            | 156 ms                                                 | 147 ms: 1.06x faster                                                        |
| xml_etree_process          | 60.4 ms                                                | 57.2 ms: 1.06x faster                                                       |
| pprint_pformat             | 1.51 sec                                               | 1.44 sec: 1.05x faster                                                      |
| bpe_tokeniser              | 4.69 sec                                               | 4.49 sec: 1.04x faster                                                      |
| json_dumps                 | 10.4 ms                                                | 9.97 ms: 1.04x faster                                                       |
| pickle_pure_python         | 300 us                                                 | 288 us: 1.04x faster                                                        |
| xml_etree_iterparse        | 102 ms                                                 | 98.2 ms: 1.04x faster                                                       |
| pyflate                    | 460 ms                                                 | 445 ms: 1.03x faster                                                        |
| regex_effbot               | 3.88 ms                                                | 3.79 ms: 1.03x faster                                                       |
| async_tree_none            | 354 ms                                                 | 347 ms: 1.02x faster                                                        |
| fannkuch                   | 381 ms                                                 | 373 ms: 1.02x faster                                                        |
| unpickle_pure_python       | 213 us                                                 | 211 us: 1.01x faster                                                        |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                        |
| gc_traversal               | 3.81 ms                                                | 3.78 ms: 1.01x faster                                                       |
| regex_dna                  | 220 ms                                                 | 221 ms: 1.00x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 24.1 ms: 1.00x slower                                                       |
| asyncio_websockets         | 555 ms                                                 | 559 ms: 1.01x slower                                                        |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.01x slower                                                       |
| regex_v8                   | 25.3 ms                                                | 25.5 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 581 ms: 1.01x slower                                                        |
| mdp                        | 2.74 sec                                               | 2.80 sec: 1.02x slower                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.83 sec: 1.02x slower                                                      |
| typing_runtime_protocols   | 159 us                                                 | 163 us: 1.03x slower                                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 558 ms: 1.03x slower                                                        |
| python_startup_no_site     | 6.99 ms                                                | 7.19 ms: 1.03x slower                                                       |
| tomli_loads                | 2.11 sec                                               | 2.18 sec: 1.03x slower                                                      |
| thrift                     | 796 us                                                 | 831 us: 1.04x slower                                                        |
| coverage                   | 83.7 ms                                                | 87.4 ms: 1.04x slower                                                       |
| scimark_sor                | 122 ms                                                 | 128 ms: 1.05x slower                                                        |
| json_loads                 | 27.0 us                                                | 28.3 us: 1.05x slower                                                       |
| comprehensions             | 16.4 us                                                | 17.3 us: 1.05x slower                                                       |
| async_generators           | 433 ms                                                 | 457 ms: 1.05x slower                                                        |
| genshi_text                | 22.9 ms                                                | 24.3 ms: 1.06x slower                                                       |
| coroutines                 | 22.5 ms                                                | 24.0 ms: 1.07x slower                                                       |
| chaos                      | 58.4 ms                                                | 62.6 ms: 1.07x slower                                                       |
| nqueens                    | 80.6 ms                                                | 86.6 ms: 1.07x slower                                                       |
| raytrace                   | 262 ms                                                 | 284 ms: 1.09x slower                                                        |
| async_tree_io_tg           | 825 ms                                                 | 896 ms: 1.09x slower                                                        |
| asyncio_tcp                | 488 ms                                                 | 531 ms: 1.09x slower                                                        |
| 2to3                       | 265 ms                                                 | 290 ms: 1.09x slower                                                        |
| pycparser                  | 1.19 sec                                               | 1.32 sec: 1.10x slower                                                      |
| logging_silent             | 102 ns                                                 | 113 ns: 1.11x slower                                                        |
| regex_compile              | 131 ms                                                 | 147 ms: 1.12x slower                                                        |
| bench_thread_pool          | 815 us                                                 | 914 us: 1.12x slower                                                        |
| create_gc_cycles           | 1.61 ms                                                | 1.81 ms: 1.12x slower                                                       |
| richards                   | 48.1 ms                                                | 54.2 ms: 1.13x slower                                                       |
| richards_super             | 54.4 ms                                                | 62.0 ms: 1.14x slower                                                       |
| async_tree_io              | 843 ms                                                 | 966 ms: 1.15x slower                                                        |
| hexiom                     | 6.13 ms                                                | 7.15 ms: 1.17x slower                                                       |
| html5lib                   | 64.5 ms                                                | 75.5 ms: 1.17x slower                                                       |
| sqlglot_normalize          | 107 ms                                                 | 128 ms: 1.19x slower                                                        |
| logging_format             | 6.25 us                                                | 7.45 us: 1.19x slower                                                       |
| generators                 | 28.8 ms                                                | 34.5 ms: 1.20x slower                                                       |
| logging_simple             | 5.66 us                                                | 6.91 us: 1.22x slower                                                       |
| django_template            | 34.4 ms                                                | 42.1 ms: 1.22x slower                                                       |
| sympy_expand               | 462 ms                                                 | 565 ms: 1.22x slower                                                        |
| sqlglot_optimize           | 53.9 ms                                                | 66.3 ms: 1.23x slower                                                       |
| sympy_str                  | 274 ms                                                 | 339 ms: 1.24x slower                                                        |
| sqlglot_parse              | 1.27 ms                                                | 1.60 ms: 1.27x slower                                                       |
| sqlglot_transpile          | 1.57 ms                                                | 2.02 ms: 1.28x slower                                                       |
| go                         | 142 ms                                                 | 182 ms: 1.28x slower                                                        |
| tornado_http               | 91.5 ms                                                | 120 ms: 1.31x slower                                                        |
| genshi_xml                 | 50.3 ms                                                | 67.5 ms: 1.34x slower                                                       |
| sympy_integrate            | 19.9 ms                                                | 27.3 ms: 1.37x slower                                                       |
| docutils                   | 2.58 sec                                               | 3.58 sec: 1.38x slower                                                      |
| deltablue                  | 3.15 ms                                                | 4.46 ms: 1.42x slower                                                       |
| sympy_sum                  | 150 ms                                                 | 213 ms: 1.42x slower                                                        |
| pylint                     | 313 ms                                                 | 486 ms: 1.55x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.05x slower                                                                |

Benchmark hidden because not significant (5): async_tree_memoization, json, pidigits, async_tree_none_tg, scimark_lu
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.48% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.15x