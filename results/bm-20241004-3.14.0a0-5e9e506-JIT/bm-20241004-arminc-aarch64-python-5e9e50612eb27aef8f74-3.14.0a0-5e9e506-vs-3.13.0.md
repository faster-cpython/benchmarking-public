# Results vs. 3.13.0

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: linux-aarch64
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.17x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 386 ms: 1.26x slower                                                    |
| docutils       | 2.91 sec                                                 | 3.71 sec: 1.28x slower                                                  |
| html5lib       | 64.3 ms                                                  | 71.9 ms: 1.12x slower                                                   |
| tornado_http   | 131 ms                                                   | 148 ms: 1.12x slower                                                    |
| Geometric mean | (ref)                                                    | 1.19x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 543 ms: 1.20x faster                                                    |
| async_tree_none_tg        | 467 ms                                                   | 423 ms: 1.10x faster                                                    |
| async_tree_none           | 493 ms                                                   | 459 ms: 1.07x faster                                                    |
| async_tree_memoization    | 626 ms                                                   | 582 ms: 1.07x faster                                                    |
| asyncio_websockets        | 656 ms                                                   | 665 ms: 1.01x slower                                                    |
| coroutines                | 28.2 ms                                                  | 28.8 ms: 1.02x slower                                                   |
| async_generators          | 496 ms                                                   | 508 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.24 sec: 1.03x slower                                                  |
| asyncio_tcp               | 568 ms                                                   | 603 ms: 1.06x slower                                                    |
| async_tree_io             | 1.11 sec                                                 | 1.20 sec: 1.08x slower                                                  |
| async_tree_io_tg          | 1.09 sec                                                 | 1.20 sec: 1.10x slower                                                  |
| Geometric mean            | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 111 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.9 ms: 1.02x faster                                                   |
| regex_effbot   | 4.87 ms                                                  | 5.00 ms: 1.03x slower                                                   |
| regex_dna      | 246 ms                                                   | 255 ms: 1.03x slower                                                    |
| regex_compile  | 128 ms                                                   | 180 ms: 1.40x slower                                                    |
| Geometric mean | (ref)                                                    | 1.10x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle             | 20.2 us                                                  | 19.3 us: 1.05x faster                                                   |
| unpickle_list        | 6.65 us                                                  | 6.56 us: 1.01x faster                                                   |
| pickle_list          | 5.34 us                                                  | 5.29 us: 1.01x faster                                                   |
| pickle               | 13.5 us                                                  | 13.7 us: 1.02x slower                                                   |
| json_dumps           | 13.4 ms                                                  | 13.6 ms: 1.02x slower                                                   |
| xml_etree_iterparse  | 147 ms                                                   | 152 ms: 1.04x slower                                                    |
| tomli_loads          | 2.53 sec                                                 | 2.65 sec: 1.05x slower                                                  |
| unpickle_pure_python | 254 us                                                   | 267 us: 1.05x slower                                                    |
| pickle_pure_python   | 359 us                                                   | 393 us: 1.09x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (5): pickle_dict, xml_etree_generate, xml_etree_parse, json_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 14.6 ms: 1.10x slower                                                   |
| Geometric mean | (ref)                                                    | 1.05x slower                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| django_template | 42.3 ms                                                  | 52.2 ms: 1.24x slower                                                   |
| genshi_text     | 27.7 ms                                                  | 34.4 ms: 1.24x slower                                                   |
| genshi_xml      | 60.2 ms                                                  | 84.4 ms: 1.40x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.20x slower                                                            |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo             | 51.0 us                                                  | 37.6 us: 1.36x faster                                                   |
| async_tree_memoization_tg | 649 ms                                                   | 543 ms: 1.20x faster                                                    |
| deepcopy                  | 451 us                                                   | 407 us: 1.11x faster                                                    |
| async_tree_none_tg        | 467 ms                                                   | 423 ms: 1.10x faster                                                    |
| async_tree_none           | 493 ms                                                   | 459 ms: 1.07x faster                                                    |
| async_tree_memoization    | 626 ms                                                   | 582 ms: 1.07x faster                                                    |
| unpickle                  | 20.2 us                                                  | 19.3 us: 1.05x faster                                                   |
| scimark_sor               | 159 ms                                                   | 153 ms: 1.04x faster                                                    |
| deepcopy_reduce           | 4.07 us                                                  | 3.94 us: 1.03x faster                                                   |
| nbody                     | 114 ms                                                   | 111 ms: 1.03x faster                                                    |
| mako                      | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| pathlib                   | 22.4 ms                                                  | 21.9 ms: 1.02x faster                                                   |
| regex_v8                  | 31.5 ms                                                  | 30.9 ms: 1.02x faster                                                   |
| unpickle_list             | 6.65 us                                                  | 6.56 us: 1.01x faster                                                   |
| pickle_list               | 5.34 us                                                  | 5.29 us: 1.01x faster                                                   |
| thrift                    | 946 us                                                   | 955 us: 1.01x slower                                                    |
| sqlite_synth              | 3.84 us                                                  | 3.89 us: 1.01x slower                                                   |
| asyncio_websockets        | 656 ms                                                   | 665 ms: 1.01x slower                                                    |
| pickle                    | 13.5 us                                                  | 13.7 us: 1.02x slower                                                   |
| json                      | 5.61 ms                                                  | 5.72 ms: 1.02x slower                                                   |
| coroutines                | 28.2 ms                                                  | 28.8 ms: 1.02x slower                                                   |
| json_dumps                | 13.4 ms                                                  | 13.6 ms: 1.02x slower                                                   |
| async_generators          | 496 ms                                                   | 508 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.24 sec: 1.03x slower                                                  |
| regex_effbot              | 4.87 ms                                                  | 5.00 ms: 1.03x slower                                                   |
| bpe_tokeniser             | 5.90 sec                                                 | 6.07 sec: 1.03x slower                                                  |
| regex_dna                 | 246 ms                                                   | 255 ms: 1.03x slower                                                    |
| xml_etree_iterparse       | 147 ms                                                   | 152 ms: 1.04x slower                                                    |
| mdp                       | 3.36 sec                                                 | 3.51 sec: 1.04x slower                                                  |
| tomli_loads               | 2.53 sec                                                 | 2.65 sec: 1.05x slower                                                  |
| unpickle_pure_python      | 254 us                                                   | 267 us: 1.05x slower                                                    |
| scimark_sparse_mat_mult   | 6.58 ms                                                  | 6.91 ms: 1.05x slower                                                   |
| asyncio_tcp               | 568 ms                                                   | 603 ms: 1.06x slower                                                    |
| logging_format            | 7.83 us                                                  | 8.34 us: 1.06x slower                                                   |
| scimark_monte_carlo       | 83.8 ms                                                  | 89.5 ms: 1.07x slower                                                   |
| spectral_norm             | 141 ms                                                   | 152 ms: 1.08x slower                                                    |
| async_tree_io             | 1.11 sec                                                 | 1.20 sec: 1.08x slower                                                  |
| scimark_lu                | 139 ms                                                   | 151 ms: 1.09x slower                                                    |
| crypto_pyaes              | 82.7 ms                                                  | 89.8 ms: 1.09x slower                                                   |
| bench_thread_pool         | 1.28 ms                                                  | 1.39 ms: 1.09x slower                                                   |
| pickle_pure_python        | 359 us                                                   | 393 us: 1.09x slower                                                    |
| logging_simple            | 7.04 us                                                  | 7.70 us: 1.09x slower                                                   |
| async_tree_io_tg          | 1.09 sec                                                 | 1.20 sec: 1.10x slower                                                  |
| typing_runtime_protocols  | 192 us                                                   | 211 us: 1.10x slower                                                    |
| python_startup            | 13.3 ms                                                  | 14.6 ms: 1.10x slower                                                   |
| meteor_contest            | 113 ms                                                   | 125 ms: 1.10x slower                                                    |
| pyflate                   | 556 ms                                                   | 616 ms: 1.11x slower                                                    |
| fannkuch                  | 452 ms                                                   | 503 ms: 1.11x slower                                                    |
| html5lib                  | 64.3 ms                                                  | 71.9 ms: 1.12x slower                                                   |
| tornado_http              | 131 ms                                                   | 148 ms: 1.12x slower                                                    |
| go                        | 163 ms                                                   | 184 ms: 1.13x slower                                                    |
| deltablue                 | 3.85 ms                                                  | 4.40 ms: 1.14x slower                                                   |
| raytrace                  | 298 ms                                                   | 351 ms: 1.18x slower                                                    |
| pycparser                 | 1.26 sec                                                 | 1.51 sec: 1.19x slower                                                  |
| sqlglot_normalize         | 128 ms                                                   | 157 ms: 1.22x slower                                                    |
| sqlglot_parse             | 1.38 ms                                                  | 1.69 ms: 1.22x slower                                                   |
| comprehensions            | 20.4 us                                                  | 25.0 us: 1.22x slower                                                   |
| django_template           | 42.3 ms                                                  | 52.2 ms: 1.24x slower                                                   |
| richards                  | 53.5 ms                                                  | 66.2 ms: 1.24x slower                                                   |
| genshi_text               | 27.7 ms                                                  | 34.4 ms: 1.24x slower                                                   |
| richards_super            | 60.3 ms                                                  | 74.9 ms: 1.24x slower                                                   |
| sqlglot_transpile         | 1.73 ms                                                  | 2.17 ms: 1.25x slower                                                   |
| 2to3                      | 306 ms                                                   | 386 ms: 1.26x slower                                                    |
| chaos                     | 68.8 ms                                                  | 87.0 ms: 1.26x slower                                                   |
| nqueens                   | 98.7 ms                                                  | 125 ms: 1.27x slower                                                    |
| docutils                  | 2.91 sec                                                 | 3.71 sec: 1.28x slower                                                  |
| sympy_expand              | 455 ms                                                   | 597 ms: 1.31x slower                                                    |
| sqlglot_optimize          | 62.4 ms                                                  | 82.8 ms: 1.33x slower                                                   |
| pprint_safe_repr          | 926 ms                                                   | 1.24 sec: 1.33x slower                                                  |
| gc_traversal              | 4.53 ms                                                  | 6.11 ms: 1.35x slower                                                   |
| sympy_str                 | 264 ms                                                   | 359 ms: 1.36x slower                                                    |
| pprint_pformat            | 1.90 sec                                                 | 2.63 sec: 1.39x slower                                                  |
| sympy_integrate           | 21.0 ms                                                  | 29.2 ms: 1.39x slower                                                   |
| genshi_xml                | 60.2 ms                                                  | 84.4 ms: 1.40x slower                                                   |
| regex_compile             | 128 ms                                                   | 180 ms: 1.40x slower                                                    |
| hexiom                    | 7.13 ms                                                  | 10.2 ms: 1.42x slower                                                   |
| pylint                    | 343 ms                                                   | 492 ms: 1.43x slower                                                    |
| sympy_sum                 | 143 ms                                                   | 214 ms: 1.49x slower                                                    |
| generators                | 37.8 ms                                                  | 59.1 ms: 1.56x slower                                                   |
| create_gc_cycles          | 2.12 ms                                                  | 3.57 ms: 1.68x slower                                                   |
| unpack_sequence           | 57.2 ns                                                  | 146 ns: 2.56x slower                                                    |
| bench_mp_pool             | 7.30 ms                                                  | 1.43 sec: 196.39x slower                                                |
| Geometric mean            | (ref)                                                    | 1.17x slower                                                            |

Benchmark hidden because not significant (14): async_tree_cpu_io_mixed_tg, pickle_dict, logging_silent, xml_etree_generate, scimark_fft, python_startup_no_site, float, async_tree_cpu_io_mixed, xml_etree_parse, json_loads, telco, pidigits, coverage, xml_etree_process
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: dulwich_log, sphinx

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.20x