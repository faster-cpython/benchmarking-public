# Results vs. 3.13.0

- fork: brandtbucher
- ref: underflow_known_dyna
- machine: linux-x86_64
- commit hash: 7ad3776
- commit date: 2024-09-06
- overall geometric mean: 1.02x slower
- HPT reliability: 68.97%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 285 ms: 1.07x slower                                                        |
| docutils       | 2.58 sec                                               | 3.25 sec: 1.26x slower                                                      |
| html5lib       | 64.5 ms                                                | 69.1 ms: 1.07x slower                                                       |
| tornado_http   | 91.5 ms                                                | 103 ms: 1.13x slower                                                        |
| Geometric mean | (ref)                                                  | 1.13x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 406 ms: 1.15x faster                                                        |
| async_tree_memoization    | 442 ms                                                 | 406 ms: 1.09x faster                                                        |
| async_tree_none           | 354 ms                                                 | 326 ms: 1.09x faster                                                        |
| async_tree_none_tg        | 320 ms                                                 | 311 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 563 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                      |
| asyncio_tcp               | 488 ms                                                 | 500 ms: 1.02x slower                                                        |
| coroutines                | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                       |
| async_generators          | 433 ms                                                 | 460 ms: 1.06x slower                                                        |
| async_tree_io_tg          | 825 ms                                                 | 900 ms: 1.09x slower                                                        |
| async_tree_io             | 843 ms                                                 | 933 ms: 1.11x slower                                                        |
| Geometric mean            | (ref)                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.9 ms: 1.11x faster                                                       |
| nbody          | 85.7 ms                                                | 79.6 ms: 1.08x faster                                                       |
| pidigits       | 186 ms                                                 | 185 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.62 ms: 1.07x faster                                                       |
| regex_v8       | 25.3 ms                                                | 24.6 ms: 1.03x faster                                                       |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                                        |
| regex_compile  | 131 ms                                                 | 151 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 77.8 ms: 1.12x faster                                                       |
| xml_etree_process    | 60.4 ms                                                | 54.3 ms: 1.11x faster                                                       |
| unpickle_pure_python | 213 us                                                 | 201 us: 1.06x faster                                                        |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.06x faster                                                        |
| tomli_loads          | 2.11 sec                                               | 2.00 sec: 1.06x faster                                                      |
| xml_etree_iterparse  | 102 ms                                                 | 98.7 ms: 1.03x faster                                                       |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                       |
| pickle               | 11.6 us                                                | 11.6 us: 1.01x slower                                                       |
| pickle_dict          | 33.2 us                                                | 34.1 us: 1.03x slower                                                       |
| pickle_pure_python   | 300 us                                                 | 310 us: 1.03x slower                                                        |
| pickle_list          | 5.01 us                                                | 5.27 us: 1.05x slower                                                       |
| json_loads           | 27.0 us                                                | 28.5 us: 1.06x slower                                                       |
| unpickle_list        | 4.96 us                                                | 5.29 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.01x slower                                                       |
| python_startup_no_site | 6.99 ms                                                | 7.17 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.70 ms: 1.14x faster                                                       |
| genshi_text     | 22.9 ms                                                | 23.9 ms: 1.04x slower                                                       |
| django_template | 34.4 ms                                                | 37.9 ms: 1.10x slower                                                       |
| genshi_xml      | 50.3 ms                                                | 63.5 ms: 1.26x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 26.0 us: 1.46x faster                                                       |
| deepcopy                  | 352 us                                                 | 263 us: 1.34x faster                                                        |
| richards_super            | 54.4 ms                                                | 42.8 ms: 1.27x faster                                                       |
| richards                  | 48.1 ms                                                | 38.4 ms: 1.25x faster                                                       |
| deepcopy_reduce           | 3.17 us                                                | 2.64 us: 1.20x faster                                                       |
| scimark_fft               | 369 ms                                                 | 309 ms: 1.19x faster                                                        |
| spectral_norm             | 115 ms                                                 | 99.9 ms: 1.15x faster                                                       |
| async_tree_memoization_tg | 465 ms                                                 | 406 ms: 1.15x faster                                                        |
| mako                      | 11.1 ms                                                | 9.70 ms: 1.14x faster                                                       |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.44 ms: 1.13x faster                                                       |
| xml_etree_generate        | 87.0 ms                                                | 77.8 ms: 1.12x faster                                                       |
| crypto_pyaes              | 73.0 ms                                                | 65.4 ms: 1.12x faster                                                       |
| xml_etree_process         | 60.4 ms                                                | 54.3 ms: 1.11x faster                                                       |
| float                     | 78.5 ms                                                | 70.9 ms: 1.11x faster                                                       |
| async_tree_memoization    | 442 ms                                                 | 406 ms: 1.09x faster                                                        |
| async_tree_none           | 354 ms                                                 | 326 ms: 1.09x faster                                                        |
| mdp                       | 2.74 sec                                               | 2.54 sec: 1.08x faster                                                      |
| telco                     | 8.45 ms                                                | 7.83 ms: 1.08x faster                                                       |
| nbody                     | 85.7 ms                                                | 79.6 ms: 1.08x faster                                                       |
| pathlib                   | 17.1 ms                                                | 15.9 ms: 1.08x faster                                                       |
| regex_effbot              | 3.88 ms                                                | 3.62 ms: 1.07x faster                                                       |
| unpickle_pure_python      | 213 us                                                 | 201 us: 1.06x faster                                                        |
| xml_etree_parse           | 156 ms                                                 | 148 ms: 1.06x faster                                                        |
| tomli_loads               | 2.11 sec                                               | 2.00 sec: 1.06x faster                                                      |
| bpe_tokeniser             | 4.69 sec                                               | 4.45 sec: 1.05x faster                                                      |
| logging_silent            | 102 ns                                                 | 97.3 ns: 1.05x faster                                                       |
| xml_etree_iterparse       | 102 ms                                                 | 98.7 ms: 1.03x faster                                                       |
| go                        | 142 ms                                                 | 138 ms: 1.03x faster                                                        |
| async_tree_none_tg        | 320 ms                                                 | 311 ms: 1.03x faster                                                        |
| regex_v8                  | 25.3 ms                                                | 24.6 ms: 1.03x faster                                                       |
| sqlite_synth              | 2.85 us                                                | 2.79 us: 1.02x faster                                                       |
| thrift                    | 796 us                                                 | 780 us: 1.02x faster                                                        |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 563 ms: 1.02x faster                                                        |
| regex_dna                 | 220 ms                                                 | 216 ms: 1.02x faster                                                        |
| meteor_contest            | 108 ms                                                 | 106 ms: 1.01x faster                                                        |
| json_dumps                | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                       |
| gc_traversal              | 3.81 ms                                                | 3.78 ms: 1.01x faster                                                       |
| pidigits                  | 186 ms                                                 | 185 ms: 1.01x faster                                                        |
| pyflate                   | 460 ms                                                 | 462 ms: 1.00x slower                                                        |
| comprehensions            | 16.4 us                                                | 16.5 us: 1.01x slower                                                       |
| pickle                    | 11.6 us                                                | 11.6 us: 1.01x slower                                                       |
| python_startup            | 10.6 ms                                                | 10.6 ms: 1.01x slower                                                       |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                      |
| scimark_sor               | 122 ms                                                 | 124 ms: 1.01x slower                                                        |
| json                      | 5.20 ms                                                | 5.27 ms: 1.01x slower                                                       |
| scimark_monte_carlo       | 66.3 ms                                                | 67.4 ms: 1.02x slower                                                       |
| asyncio_tcp               | 488 ms                                                 | 500 ms: 1.02x slower                                                        |
| logging_format            | 6.25 us                                                | 6.42 us: 1.03x slower                                                       |
| typing_runtime_protocols  | 159 us                                                 | 163 us: 1.03x slower                                                        |
| python_startup_no_site    | 6.99 ms                                                | 7.17 ms: 1.03x slower                                                       |
| pickle_dict               | 33.2 us                                                | 34.1 us: 1.03x slower                                                       |
| deltablue                 | 3.15 ms                                                | 3.24 ms: 1.03x slower                                                       |
| coroutines                | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                       |
| pickle_pure_python        | 300 us                                                 | 310 us: 1.03x slower                                                        |
| bench_thread_pool         | 815 us                                                 | 846 us: 1.04x slower                                                        |
| coverage                  | 83.7 ms                                                | 87.0 ms: 1.04x slower                                                       |
| nqueens                   | 80.6 ms                                                | 83.8 ms: 1.04x slower                                                       |
| logging_simple            | 5.66 us                                                | 5.91 us: 1.04x slower                                                       |
| genshi_text               | 22.9 ms                                                | 23.9 ms: 1.04x slower                                                       |
| raytrace                  | 262 ms                                                 | 275 ms: 1.05x slower                                                        |
| pickle_list               | 5.01 us                                                | 5.27 us: 1.05x slower                                                       |
| json_loads                | 27.0 us                                                | 28.5 us: 1.06x slower                                                       |
| async_generators          | 433 ms                                                 | 460 ms: 1.06x slower                                                        |
| unpickle_list             | 4.96 us                                                | 5.29 us: 1.07x slower                                                       |
| pycparser                 | 1.19 sec                                               | 1.27 sec: 1.07x slower                                                      |
| html5lib                  | 64.5 ms                                                | 69.1 ms: 1.07x slower                                                       |
| 2to3                      | 265 ms                                                 | 285 ms: 1.07x slower                                                        |
| async_tree_io_tg          | 825 ms                                                 | 900 ms: 1.09x slower                                                        |
| django_template           | 34.4 ms                                                | 37.9 ms: 1.10x slower                                                       |
| sqlglot_normalize         | 107 ms                                                 | 119 ms: 1.11x slower                                                        |
| async_tree_io             | 843 ms                                                 | 933 ms: 1.11x slower                                                        |
| create_gc_cycles          | 1.61 ms                                                | 1.78 ms: 1.11x slower                                                       |
| sqlglot_optimize          | 53.9 ms                                                | 60.1 ms: 1.11x slower                                                       |
| hexiom                    | 6.13 ms                                                | 6.86 ms: 1.12x slower                                                       |
| sqlglot_transpile         | 1.57 ms                                                | 1.78 ms: 1.13x slower                                                       |
| tornado_http              | 91.5 ms                                                | 103 ms: 1.13x slower                                                        |
| sympy_expand              | 462 ms                                                 | 530 ms: 1.15x slower                                                        |
| regex_compile             | 131 ms                                                 | 151 ms: 1.15x slower                                                        |
| generators                | 28.8 ms                                                | 33.2 ms: 1.15x slower                                                       |
| sympy_str                 | 274 ms                                                 | 319 ms: 1.17x slower                                                        |
| dulwich_log               | 63.0 ms                                                | 74.1 ms: 1.18x slower                                                       |
| sqlglot_parse             | 1.27 ms                                                | 1.52 ms: 1.20x slower                                                       |
| sympy_integrate           | 19.9 ms                                                | 24.9 ms: 1.25x slower                                                       |
| docutils                  | 2.58 sec                                               | 3.25 sec: 1.26x slower                                                      |
| genshi_xml                | 50.3 ms                                                | 63.5 ms: 1.26x slower                                                       |
| sympy_sum                 | 150 ms                                                 | 189 ms: 1.27x slower                                                        |
| pylint                    | 313 ms                                                 | 416 ms: 1.33x slower                                                        |
| unpack_sequence           | 42.4 ns                                                | 110 ns: 2.59x slower                                                        |
| Geometric mean            | (ref)                                                  | 1.02x slower                                                                |

Benchmark hidden because not significant (9): pprint_safe_repr, scimark_lu, pprint_pformat, asyncio_websockets, bench_mp_pool, chaos, fannkuch, async_tree_cpu_io_mixed_tg, unpickle
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 68.97% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.11x