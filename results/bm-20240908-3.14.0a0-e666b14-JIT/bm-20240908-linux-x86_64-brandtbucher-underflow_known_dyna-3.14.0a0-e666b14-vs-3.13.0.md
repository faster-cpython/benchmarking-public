# Results vs. 3.13.0

- fork: brandtbucher
- ref: underflow_known_dyna
- machine: linux-x86_64
- commit hash: e666b14
- commit date: 2024-09-08
- overall geometric mean: 1.02x slower
- HPT reliability: 68.02%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 288 ms: 1.09x slower                                                        |
| docutils       | 2.58 sec                                               | 3.23 sec: 1.25x slower                                                      |
| html5lib       | 64.5 ms                                                | 67.7 ms: 1.05x slower                                                       |
| tornado_http   | 91.5 ms                                                | 104 ms: 1.14x slower                                                        |
| Geometric mean | (ref)                                                  | 1.13x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 412 ms: 1.13x faster                                                        |
| async_tree_none           | 354 ms                                                 | 326 ms: 1.09x faster                                                        |
| async_tree_memoization    | 442 ms                                                 | 416 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 561 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                      |
| coroutines                | 22.5 ms                                                | 22.8 ms: 1.01x slower                                                       |
| asyncio_tcp               | 488 ms                                                 | 506 ms: 1.04x slower                                                        |
| async_generators          | 433 ms                                                 | 452 ms: 1.04x slower                                                        |
| async_tree_io_tg          | 825 ms                                                 | 910 ms: 1.10x slower                                                        |
| async_tree_io             | 843 ms                                                 | 938 ms: 1.11x slower                                                        |
| Geometric mean            | (ref)                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (3): async_tree_none_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 71.4 ms: 1.10x faster                                                       |
| nbody          | 85.7 ms                                                | 80.7 ms: 1.06x faster                                                       |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.59 ms: 1.08x faster                                                       |
| regex_dna      | 220 ms                                                 | 212 ms: 1.04x faster                                                        |
| regex_v8       | 25.3 ms                                                | 25.3 ms: 1.00x slower                                                       |
| regex_compile  | 131 ms                                                 | 154 ms: 1.17x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 77.2 ms: 1.13x faster                                                       |
| xml_etree_process    | 60.4 ms                                                | 53.9 ms: 1.12x faster                                                       |
| xml_etree_parse      | 156 ms                                                 | 145 ms: 1.07x faster                                                        |
| unpickle_pure_python | 213 us                                                 | 201 us: 1.06x faster                                                        |
| xml_etree_iterparse  | 102 ms                                                 | 98.3 ms: 1.04x faster                                                       |
| tomli_loads          | 2.11 sec                                               | 2.07 sec: 1.02x faster                                                      |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                       |
| pickle               | 11.6 us                                                | 11.5 us: 1.01x faster                                                       |
| pickle_dict          | 33.2 us                                                | 34.7 us: 1.05x slower                                                       |
| unpickle_list        | 4.96 us                                                | 5.24 us: 1.06x slower                                                       |
| pickle_list          | 5.01 us                                                | 5.29 us: 1.06x slower                                                       |
| json_loads           | 27.0 us                                                | 28.9 us: 1.07x slower                                                       |
| pickle_pure_python   | 300 us                                                 | 330 us: 1.10x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.01x slower                                                       |
| python_startup_no_site | 6.99 ms                                                | 7.17 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.75 ms: 1.14x faster                                                       |
| django_template | 34.4 ms                                                | 37.8 ms: 1.10x slower                                                       |
| genshi_xml      | 50.3 ms                                                | 58.7 ms: 1.17x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                                |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 25.2 us: 1.51x faster                                                       |
| deepcopy                  | 352 us                                                 | 267 us: 1.32x faster                                                        |
| richards_super            | 54.4 ms                                                | 44.3 ms: 1.23x faster                                                       |
| richards                  | 48.1 ms                                                | 39.4 ms: 1.22x faster                                                       |
| scimark_fft               | 369 ms                                                 | 311 ms: 1.19x faster                                                        |
| deepcopy_reduce           | 3.17 us                                                | 2.71 us: 1.17x faster                                                       |
| spectral_norm             | 115 ms                                                 | 100 ms: 1.15x faster                                                        |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.41 ms: 1.14x faster                                                       |
| mako                      | 11.1 ms                                                | 9.75 ms: 1.14x faster                                                       |
| async_tree_memoization_tg | 465 ms                                                 | 412 ms: 1.13x faster                                                        |
| xml_etree_generate        | 87.0 ms                                                | 77.2 ms: 1.13x faster                                                       |
| xml_etree_process         | 60.4 ms                                                | 53.9 ms: 1.12x faster                                                       |
| float                     | 78.5 ms                                                | 71.4 ms: 1.10x faster                                                       |
| crypto_pyaes              | 73.0 ms                                                | 66.5 ms: 1.10x faster                                                       |
| async_tree_none           | 354 ms                                                 | 326 ms: 1.09x faster                                                        |
| mdp                       | 2.74 sec                                               | 2.54 sec: 1.08x faster                                                      |
| regex_effbot              | 3.88 ms                                                | 3.59 ms: 1.08x faster                                                       |
| pathlib                   | 17.1 ms                                                | 15.9 ms: 1.07x faster                                                       |
| xml_etree_parse           | 156 ms                                                 | 145 ms: 1.07x faster                                                        |
| nbody                     | 85.7 ms                                                | 80.7 ms: 1.06x faster                                                       |
| async_tree_memoization    | 442 ms                                                 | 416 ms: 1.06x faster                                                        |
| unpickle_pure_python      | 213 us                                                 | 201 us: 1.06x faster                                                        |
| telco                     | 8.45 ms                                                | 8.02 ms: 1.05x faster                                                       |
| go                        | 142 ms                                                 | 135 ms: 1.05x faster                                                        |
| regex_dna                 | 220 ms                                                 | 212 ms: 1.04x faster                                                        |
| xml_etree_iterparse       | 102 ms                                                 | 98.3 ms: 1.04x faster                                                       |
| sqlite_synth              | 2.85 us                                                | 2.75 us: 1.04x faster                                                       |
| scimark_lu                | 115 ms                                                 | 111 ms: 1.04x faster                                                        |
| bpe_tokeniser             | 4.69 sec                                               | 4.55 sec: 1.03x faster                                                      |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 561 ms: 1.02x faster                                                        |
| fannkuch                  | 381 ms                                                 | 373 ms: 1.02x faster                                                        |
| tomli_loads               | 2.11 sec                                               | 2.07 sec: 1.02x faster                                                      |
| thrift                    | 796 us                                                 | 782 us: 1.02x faster                                                        |
| meteor_contest            | 108 ms                                                 | 106 ms: 1.02x faster                                                        |
| chaos                     | 58.4 ms                                                | 57.5 ms: 1.02x faster                                                       |
| json_dumps                | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                       |
| scimark_sor               | 122 ms                                                 | 121 ms: 1.01x faster                                                        |
| gc_traversal              | 3.81 ms                                                | 3.77 ms: 1.01x faster                                                       |
| pprint_pformat            | 1.51 sec                                               | 1.50 sec: 1.01x faster                                                      |
| pickle                    | 11.6 us                                                | 11.5 us: 1.01x faster                                                       |
| regex_v8                  | 25.3 ms                                                | 25.3 ms: 1.00x slower                                                       |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                      |
| pidigits                  | 186 ms                                                 | 187 ms: 1.01x slower                                                        |
| python_startup            | 10.6 ms                                                | 10.6 ms: 1.01x slower                                                       |
| comprehensions            | 16.4 us                                                | 16.5 us: 1.01x slower                                                       |
| coroutines                | 22.5 ms                                                | 22.8 ms: 1.01x slower                                                       |
| logging_format            | 6.25 us                                                | 6.36 us: 1.02x slower                                                       |
| coverage                  | 83.7 ms                                                | 85.2 ms: 1.02x slower                                                       |
| python_startup_no_site    | 6.99 ms                                                | 7.17 ms: 1.03x slower                                                       |
| bench_thread_pool         | 815 us                                                 | 837 us: 1.03x slower                                                        |
| json                      | 5.20 ms                                                | 5.36 ms: 1.03x slower                                                       |
| asyncio_tcp               | 488 ms                                                 | 506 ms: 1.04x slower                                                        |
| logging_simple            | 5.66 us                                                | 5.89 us: 1.04x slower                                                       |
| deltablue                 | 3.15 ms                                                | 3.28 ms: 1.04x slower                                                       |
| nqueens                   | 80.6 ms                                                | 84.0 ms: 1.04x slower                                                       |
| async_generators          | 433 ms                                                 | 452 ms: 1.04x slower                                                        |
| pickle_dict               | 33.2 us                                                | 34.7 us: 1.05x slower                                                       |
| html5lib                  | 64.5 ms                                                | 67.7 ms: 1.05x slower                                                       |
| typing_runtime_protocols  | 159 us                                                 | 168 us: 1.05x slower                                                        |
| unpickle_list             | 4.96 us                                                | 5.24 us: 1.06x slower                                                       |
| pickle_list               | 5.01 us                                                | 5.29 us: 1.06x slower                                                       |
| json_loads                | 27.0 us                                                | 28.9 us: 1.07x slower                                                       |
| logging_silent            | 102 ns                                                 | 109 ns: 1.07x slower                                                        |
| scimark_monte_carlo       | 66.3 ms                                                | 71.4 ms: 1.08x slower                                                       |
| raytrace                  | 262 ms                                                 | 284 ms: 1.09x slower                                                        |
| 2to3                      | 265 ms                                                 | 288 ms: 1.09x slower                                                        |
| django_template           | 34.4 ms                                                | 37.8 ms: 1.10x slower                                                       |
| pickle_pure_python        | 300 us                                                 | 330 us: 1.10x slower                                                        |
| create_gc_cycles          | 1.61 ms                                                | 1.77 ms: 1.10x slower                                                       |
| async_tree_io_tg          | 825 ms                                                 | 910 ms: 1.10x slower                                                        |
| pycparser                 | 1.19 sec                                               | 1.32 sec: 1.11x slower                                                      |
| sqlglot_transpile         | 1.57 ms                                                | 1.75 ms: 1.11x slower                                                       |
| async_tree_io             | 843 ms                                                 | 938 ms: 1.11x slower                                                        |
| sqlglot_normalize         | 107 ms                                                 | 121 ms: 1.13x slower                                                        |
| tornado_http              | 91.5 ms                                                | 104 ms: 1.14x slower                                                        |
| sqlglot_optimize          | 53.9 ms                                                | 61.6 ms: 1.14x slower                                                       |
| generators                | 28.8 ms                                                | 33.2 ms: 1.15x slower                                                       |
| sympy_expand              | 462 ms                                                 | 533 ms: 1.15x slower                                                        |
| genshi_xml                | 50.3 ms                                                | 58.7 ms: 1.17x slower                                                       |
| regex_compile             | 131 ms                                                 | 154 ms: 1.17x slower                                                        |
| sympy_str                 | 274 ms                                                 | 322 ms: 1.18x slower                                                        |
| sqlglot_parse             | 1.27 ms                                                | 1.49 ms: 1.18x slower                                                       |
| dulwich_log               | 63.0 ms                                                | 75.4 ms: 1.20x slower                                                       |
| hexiom                    | 6.13 ms                                                | 7.42 ms: 1.21x slower                                                       |
| docutils                  | 2.58 sec                                               | 3.23 sec: 1.25x slower                                                      |
| sympy_integrate           | 19.9 ms                                                | 24.9 ms: 1.25x slower                                                       |
| sympy_sum                 | 150 ms                                                 | 190 ms: 1.27x slower                                                        |
| pylint                    | 313 ms                                                 | 412 ms: 1.32x slower                                                        |
| unpack_sequence           | 42.4 ns                                                | 145 ns: 3.42x slower                                                        |
| Geometric mean            | (ref)                                                  | 1.02x slower                                                                |

Benchmark hidden because not significant (8): async_tree_none_tg, genshi_text, pyflate, asyncio_websockets, bench_mp_pool, unpickle, pprint_safe_repr, async_tree_cpu_io_mixed_tg
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 68.02% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.13x