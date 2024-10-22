# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_likely
- machine: linux-aarch64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.18x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 382 ms: 1.25x slower                                                    |
| docutils       | 2.91 sec                                                 | 3.58 sec: 1.23x slower                                                  |
| html5lib       | 64.3 ms                                                  | 71.9 ms: 1.12x slower                                                   |
| tornado_http   | 131 ms                                                   | 147 ms: 1.12x slower                                                    |
| Geometric mean | (ref)                                                    | 1.18x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 536 ms: 1.21x faster                                                    |
| async_tree_none           | 493 ms                                                   | 457 ms: 1.08x faster                                                    |
| async_tree_none_tg        | 467 ms                                                   | 446 ms: 1.05x faster                                                    |
| async_tree_memoization    | 626 ms                                                   | 600 ms: 1.04x faster                                                    |
| asyncio_websockets        | 656 ms                                                   | 663 ms: 1.01x slower                                                    |
| coroutines                | 28.2 ms                                                  | 28.9 ms: 1.02x slower                                                   |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.26 sec: 1.04x slower                                                  |
| async_generators          | 496 ms                                                   | 515 ms: 1.04x slower                                                    |
| async_tree_io             | 1.11 sec                                                 | 1.18 sec: 1.07x slower                                                  |
| asyncio_tcp               | 568 ms                                                   | 621 ms: 1.09x slower                                                    |
| async_tree_io_tg          | 1.09 sec                                                 | 1.25 sec: 1.14x slower                                                  |
| Geometric mean            | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 97.8 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                    | 1.02x slower                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 31.0 ms: 1.02x faster                                                   |
| regex_effbot   | 4.87 ms                                                  | 4.96 ms: 1.02x slower                                                   |
| regex_dna      | 246 ms                                                   | 254 ms: 1.03x slower                                                    |
| regex_compile  | 128 ms                                                   | 179 ms: 1.40x slower                                                    |
| Geometric mean | (ref)                                                    | 1.10x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_list        | 6.65 us                                                  | 6.42 us: 1.04x faster                                                   |
| unpickle             | 20.2 us                                                  | 19.6 us: 1.03x faster                                                   |
| pickle_list          | 5.34 us                                                  | 5.27 us: 1.01x faster                                                   |
| xml_etree_iterparse  | 147 ms                                                   | 150 ms: 1.02x slower                                                    |
| pickle               | 13.5 us                                                  | 13.9 us: 1.03x slower                                                   |
| tomli_loads          | 2.53 sec                                                 | 2.66 sec: 1.05x slower                                                  |
| unpickle_pure_python | 254 us                                                   | 270 us: 1.06x slower                                                    |
| json_dumps           | 13.4 ms                                                  | 14.6 ms: 1.09x slower                                                   |
| pickle_pure_python   | 359 us                                                   | 392 us: 1.09x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.02x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_generate, pickle_dict, json_loads, xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 14.5 ms: 1.10x slower                                                   |
| Geometric mean | (ref)                                                    | 1.05x slower                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 13.6 ms: 1.02x slower                                                   |
| genshi_text     | 27.7 ms                                                  | 34.1 ms: 1.23x slower                                                   |
| django_template | 42.3 ms                                                  | 52.6 ms: 1.24x slower                                                   |
| genshi_xml      | 60.2 ms                                                  | 83.9 ms: 1.39x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.21x slower                                                            |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo             | 51.0 us                                                  | 39.3 us: 1.30x faster                                                   |
| async_tree_memoization_tg | 649 ms                                                   | 536 ms: 1.21x faster                                                    |
| deepcopy                  | 451 us                                                   | 380 us: 1.19x faster                                                    |
| async_tree_none           | 493 ms                                                   | 457 ms: 1.08x faster                                                    |
| async_tree_none_tg        | 467 ms                                                   | 446 ms: 1.05x faster                                                    |
| async_tree_memoization    | 626 ms                                                   | 600 ms: 1.04x faster                                                    |
| unpickle_list             | 6.65 us                                                  | 6.42 us: 1.04x faster                                                   |
| scimark_sor               | 159 ms                                                   | 154 ms: 1.03x faster                                                    |
| pathlib                   | 22.4 ms                                                  | 21.8 ms: 1.03x faster                                                   |
| unpickle                  | 20.2 us                                                  | 19.6 us: 1.03x faster                                                   |
| deepcopy_reduce           | 4.07 us                                                  | 3.98 us: 1.02x faster                                                   |
| logging_silent            | 135 ns                                                   | 133 ns: 1.02x faster                                                    |
| regex_v8                  | 31.5 ms                                                  | 31.0 ms: 1.02x faster                                                   |
| pickle_list               | 5.34 us                                                  | 5.27 us: 1.01x faster                                                   |
| telco                     | 9.73 ms                                                  | 9.64 ms: 1.01x faster                                                   |
| bpe_tokeniser             | 5.90 sec                                                 | 5.96 sec: 1.01x slower                                                  |
| asyncio_websockets        | 656 ms                                                   | 663 ms: 1.01x slower                                                    |
| scimark_fft               | 447 ms                                                   | 455 ms: 1.02x slower                                                    |
| mako                      | 13.3 ms                                                  | 13.6 ms: 1.02x slower                                                   |
| regex_effbot              | 4.87 ms                                                  | 4.96 ms: 1.02x slower                                                   |
| xml_etree_iterparse       | 147 ms                                                   | 150 ms: 1.02x slower                                                    |
| coroutines                | 28.2 ms                                                  | 28.9 ms: 1.02x slower                                                   |
| regex_dna                 | 246 ms                                                   | 254 ms: 1.03x slower                                                    |
| thrift                    | 946 us                                                   | 975 us: 1.03x slower                                                    |
| pickle                    | 13.5 us                                                  | 13.9 us: 1.03x slower                                                   |
| float                     | 94.4 ms                                                  | 97.8 ms: 1.04x slower                                                   |
| logging_format            | 7.83 us                                                  | 8.12 us: 1.04x slower                                                   |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.26 sec: 1.04x slower                                                  |
| async_generators          | 496 ms                                                   | 515 ms: 1.04x slower                                                    |
| mdp                       | 3.36 sec                                                 | 3.50 sec: 1.04x slower                                                  |
| sqlite_synth              | 3.84 us                                                  | 4.00 us: 1.04x slower                                                   |
| tomli_loads               | 2.53 sec                                                 | 2.66 sec: 1.05x slower                                                  |
| scimark_monte_carlo       | 83.8 ms                                                  | 88.7 ms: 1.06x slower                                                   |
| unpickle_pure_python      | 254 us                                                   | 270 us: 1.06x slower                                                    |
| scimark_lu                | 139 ms                                                   | 148 ms: 1.06x slower                                                    |
| logging_simple            | 7.04 us                                                  | 7.49 us: 1.06x slower                                                   |
| async_tree_io             | 1.11 sec                                                 | 1.18 sec: 1.07x slower                                                  |
| crypto_pyaes              | 82.7 ms                                                  | 89.2 ms: 1.08x slower                                                   |
| bench_thread_pool         | 1.28 ms                                                  | 1.38 ms: 1.08x slower                                                   |
| meteor_contest            | 113 ms                                                   | 124 ms: 1.09x slower                                                    |
| json_dumps                | 13.4 ms                                                  | 14.6 ms: 1.09x slower                                                   |
| pickle_pure_python        | 359 us                                                   | 392 us: 1.09x slower                                                    |
| spectral_norm             | 141 ms                                                   | 154 ms: 1.09x slower                                                    |
| asyncio_tcp               | 568 ms                                                   | 621 ms: 1.09x slower                                                    |
| python_startup            | 13.3 ms                                                  | 14.5 ms: 1.10x slower                                                   |
| scimark_sparse_mat_mult   | 6.58 ms                                                  | 7.23 ms: 1.10x slower                                                   |
| tornado_http              | 131 ms                                                   | 147 ms: 1.12x slower                                                    |
| html5lib                  | 64.3 ms                                                  | 71.9 ms: 1.12x slower                                                   |
| fannkuch                  | 452 ms                                                   | 512 ms: 1.13x slower                                                    |
| typing_runtime_protocols  | 192 us                                                   | 219 us: 1.14x slower                                                    |
| async_tree_io_tg          | 1.09 sec                                                 | 1.25 sec: 1.14x slower                                                  |
| go                        | 163 ms                                                   | 187 ms: 1.15x slower                                                    |
| pyflate                   | 556 ms                                                   | 642 ms: 1.15x slower                                                    |
| deltablue                 | 3.85 ms                                                  | 4.50 ms: 1.17x slower                                                   |
| raytrace                  | 298 ms                                                   | 352 ms: 1.18x slower                                                    |
| richards_super            | 60.3 ms                                                  | 72.2 ms: 1.20x slower                                                   |
| pycparser                 | 1.26 sec                                                 | 1.52 sec: 1.20x slower                                                  |
| richards                  | 53.5 ms                                                  | 64.6 ms: 1.21x slower                                                   |
| comprehensions            | 20.4 us                                                  | 24.8 us: 1.22x slower                                                   |
| genshi_text               | 27.7 ms                                                  | 34.1 ms: 1.23x slower                                                   |
| docutils                  | 2.91 sec                                                 | 3.58 sec: 1.23x slower                                                  |
| sqlglot_normalize         | 128 ms                                                   | 159 ms: 1.24x slower                                                    |
| sqlglot_parse             | 1.38 ms                                                  | 1.71 ms: 1.24x slower                                                   |
| django_template           | 42.3 ms                                                  | 52.6 ms: 1.24x slower                                                   |
| chaos                     | 68.8 ms                                                  | 85.7 ms: 1.24x slower                                                   |
| 2to3                      | 306 ms                                                   | 382 ms: 1.25x slower                                                    |
| nqueens                   | 98.7 ms                                                  | 124 ms: 1.26x slower                                                    |
| sympy_expand              | 455 ms                                                   | 589 ms: 1.30x slower                                                    |
| sqlglot_transpile         | 1.73 ms                                                  | 2.25 ms: 1.30x slower                                                   |
| pprint_safe_repr          | 926 ms                                                   | 1.23 sec: 1.33x slower                                                  |
| sqlglot_optimize          | 62.4 ms                                                  | 83.1 ms: 1.33x slower                                                   |
| sympy_str                 | 264 ms                                                   | 356 ms: 1.35x slower                                                    |
| gc_traversal              | 4.53 ms                                                  | 6.24 ms: 1.38x slower                                                   |
| pprint_pformat            | 1.90 sec                                                 | 2.62 sec: 1.38x slower                                                  |
| genshi_xml                | 60.2 ms                                                  | 83.9 ms: 1.39x slower                                                   |
| regex_compile             | 128 ms                                                   | 179 ms: 1.40x slower                                                    |
| sympy_integrate           | 21.0 ms                                                  | 29.3 ms: 1.40x slower                                                   |
| pylint                    | 343 ms                                                   | 492 ms: 1.43x slower                                                    |
| hexiom                    | 7.13 ms                                                  | 10.3 ms: 1.44x slower                                                   |
| sympy_sum                 | 143 ms                                                   | 214 ms: 1.49x slower                                                    |
| generators                | 37.8 ms                                                  | 59.1 ms: 1.56x slower                                                   |
| create_gc_cycles          | 2.12 ms                                                  | 3.73 ms: 1.76x slower                                                   |
| unpack_sequence           | 57.2 ns                                                  | 145 ns: 2.54x slower                                                    |
| bench_mp_pool             | 7.30 ms                                                  | 2.25 sec: 308.40x slower                                                |
| Geometric mean            | (ref)                                                    | 1.18x slower                                                            |

Benchmark hidden because not significant (12): xml_etree_generate, pickle_dict, async_tree_cpu_io_mixed, python_startup_no_site, coverage, json, pidigits, json_loads, async_tree_cpu_io_mixed_tg, nbody, xml_etree_parse, xml_etree_process
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241018-3.14.0a1+-bad9944-JIT/bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944.json: dulwich_log, sphinx

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.20x