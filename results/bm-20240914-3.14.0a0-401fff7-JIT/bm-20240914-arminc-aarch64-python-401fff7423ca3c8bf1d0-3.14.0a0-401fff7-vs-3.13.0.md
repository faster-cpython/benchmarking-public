# Results vs. 3.13.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-aarch64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.10x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 380 ms: 1.24x slower                                                    |
| docutils       | 2.91 sec                                                 | 3.98 sec: 1.37x slower                                                  |
| html5lib       | 64.3 ms                                                  | 71.3 ms: 1.11x slower                                                   |
| tornado_http   | 131 ms                                                   | 147 ms: 1.12x slower                                                    |
| Geometric mean | (ref)                                                    | 1.21x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 564 ms: 1.15x faster                                                    |
| async_tree_none           | 493 ms                                                   | 444 ms: 1.11x faster                                                    |
| async_tree_none_tg        | 467 ms                                                   | 426 ms: 1.10x faster                                                    |
| async_tree_memoization    | 626 ms                                                   | 588 ms: 1.06x faster                                                    |
| asyncio_websockets        | 656 ms                                                   | 663 ms: 1.01x slower                                                    |
| coroutines                | 28.2 ms                                                  | 28.6 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.25 sec: 1.03x slower                                                  |
| async_tree_io             | 1.11 sec                                                 | 1.14 sec: 1.04x slower                                                  |
| async_tree_io_tg          | 1.09 sec                                                 | 1.17 sec: 1.07x slower                                                  |
| asyncio_tcp               | 568 ms                                                   | 619 ms: 1.09x slower                                                    |
| Geometric mean            | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 87.5 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 246 ms                                                   | 242 ms: 1.02x faster                                                    |
| regex_compile  | 128 ms                                                   | 190 ms: 1.48x slower                                                    |
| Geometric mean | (ref)                                                    | 1.10x slower                                                            |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle             | 20.2 us                                                  | 19.4 us: 1.04x faster                                                   |
| unpickle_list        | 6.65 us                                                  | 6.41 us: 1.04x faster                                                   |
| pickle_list          | 5.34 us                                                  | 5.22 us: 1.02x faster                                                   |
| json_dumps           | 13.4 ms                                                  | 13.5 ms: 1.01x slower                                                   |
| xml_etree_iterparse  | 147 ms                                                   | 149 ms: 1.02x slower                                                    |
| pickle               | 13.5 us                                                  | 13.8 us: 1.02x slower                                                   |
| tomli_loads          | 2.53 sec                                                 | 2.63 sec: 1.04x slower                                                  |
| unpickle_pure_python | 254 us                                                   | 267 us: 1.05x slower                                                    |
| pickle_pure_python   | 359 us                                                   | 380 us: 1.06x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_generate, xml_etree_process, pickle_dict, json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| django_template | 42.3 ms                                                  | 50.8 ms: 1.20x slower                                                   |
| genshi_text     | 27.7 ms                                                  | 35.7 ms: 1.29x slower                                                   |
| genshi_xml      | 60.2 ms                                                  | 82.2 ms: 1.37x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.20x slower                                                            |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo             | 51.0 us                                                  | 37.2 us: 1.37x faster                                                   |
| async_tree_memoization_tg | 649 ms                                                   | 564 ms: 1.15x faster                                                    |
| deepcopy                  | 451 us                                                   | 394 us: 1.15x faster                                                    |
| async_tree_none           | 493 ms                                                   | 444 ms: 1.11x faster                                                    |
| async_tree_none_tg        | 467 ms                                                   | 426 ms: 1.10x faster                                                    |
| float                     | 94.4 ms                                                  | 87.5 ms: 1.08x faster                                                   |
| async_tree_memoization    | 626 ms                                                   | 588 ms: 1.06x faster                                                    |
| deepcopy_reduce           | 4.07 us                                                  | 3.86 us: 1.05x faster                                                   |
| scimark_sor               | 159 ms                                                   | 152 ms: 1.05x faster                                                    |
| pathlib                   | 22.4 ms                                                  | 21.5 ms: 1.04x faster                                                   |
| unpickle                  | 20.2 us                                                  | 19.4 us: 1.04x faster                                                   |
| unpickle_list             | 6.65 us                                                  | 6.41 us: 1.04x faster                                                   |
| pickle_list               | 5.34 us                                                  | 5.22 us: 1.02x faster                                                   |
| python_startup            | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| mako                      | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| regex_dna                 | 246 ms                                                   | 242 ms: 1.02x faster                                                    |
| bpe_tokeniser             | 5.90 sec                                                 | 5.94 sec: 1.01x slower                                                  |
| asyncio_websockets        | 656 ms                                                   | 663 ms: 1.01x slower                                                    |
| json_dumps                | 13.4 ms                                                  | 13.5 ms: 1.01x slower                                                   |
| coroutines                | 28.2 ms                                                  | 28.6 ms: 1.01x slower                                                   |
| xml_etree_iterparse       | 147 ms                                                   | 149 ms: 1.02x slower                                                    |
| coverage                  | 98.5 ms                                                  | 101 ms: 1.02x slower                                                    |
| pickle                    | 13.5 us                                                  | 13.8 us: 1.02x slower                                                   |
| json                      | 5.61 ms                                                  | 5.73 ms: 1.02x slower                                                   |
| scimark_fft               | 447 ms                                                   | 459 ms: 1.03x slower                                                    |
| spectral_norm             | 141 ms                                                   | 145 ms: 1.03x slower                                                    |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.25 sec: 1.03x slower                                                  |
| logging_silent            | 135 ns                                                   | 140 ns: 1.03x slower                                                    |
| async_tree_io             | 1.11 sec                                                 | 1.14 sec: 1.04x slower                                                  |
| scimark_sparse_mat_mult   | 6.58 ms                                                  | 6.82 ms: 1.04x slower                                                   |
| bench_mp_pool             | 7.30 ms                                                  | 7.57 ms: 1.04x slower                                                   |
| thrift                    | 946 us                                                   | 981 us: 1.04x slower                                                    |
| tomli_loads               | 2.53 sec                                                 | 2.63 sec: 1.04x slower                                                  |
| mdp                       | 3.36 sec                                                 | 3.50 sec: 1.04x slower                                                  |
| logging_format            | 7.83 us                                                  | 8.20 us: 1.05x slower                                                   |
| unpickle_pure_python      | 254 us                                                   | 267 us: 1.05x slower                                                    |
| pickle_pure_python        | 359 us                                                   | 380 us: 1.06x slower                                                    |
| bench_thread_pool         | 1.28 ms                                                  | 1.36 ms: 1.06x slower                                                   |
| logging_simple            | 7.04 us                                                  | 7.52 us: 1.07x slower                                                   |
| scimark_lu                | 139 ms                                                   | 149 ms: 1.07x slower                                                    |
| async_tree_io_tg          | 1.09 sec                                                 | 1.17 sec: 1.07x slower                                                  |
| telco                     | 9.73 ms                                                  | 10.5 ms: 1.08x slower                                                   |
| typing_runtime_protocols  | 192 us                                                   | 207 us: 1.08x slower                                                    |
| create_gc_cycles          | 2.12 ms                                                  | 2.29 ms: 1.08x slower                                                   |
| crypto_pyaes              | 82.7 ms                                                  | 89.4 ms: 1.08x slower                                                   |
| asyncio_tcp               | 568 ms                                                   | 619 ms: 1.09x slower                                                    |
| meteor_contest            | 113 ms                                                   | 124 ms: 1.10x slower                                                    |
| scimark_monte_carlo       | 83.8 ms                                                  | 92.5 ms: 1.10x slower                                                   |
| html5lib                  | 64.3 ms                                                  | 71.3 ms: 1.11x slower                                                   |
| fannkuch                  | 452 ms                                                   | 503 ms: 1.11x slower                                                    |
| tornado_http              | 131 ms                                                   | 147 ms: 1.12x slower                                                    |
| gc_traversal              | 4.53 ms                                                  | 5.10 ms: 1.12x slower                                                   |
| deltablue                 | 3.85 ms                                                  | 4.36 ms: 1.13x slower                                                   |
| go                        | 163 ms                                                   | 186 ms: 1.14x slower                                                    |
| pyflate                   | 556 ms                                                   | 654 ms: 1.18x slower                                                    |
| raytrace                  | 298 ms                                                   | 350 ms: 1.18x slower                                                    |
| sqlglot_normalize         | 128 ms                                                   | 151 ms: 1.18x slower                                                    |
| comprehensions            | 20.4 us                                                  | 24.5 us: 1.20x slower                                                   |
| django_template           | 42.3 ms                                                  | 50.8 ms: 1.20x slower                                                   |
| pycparser                 | 1.26 sec                                                 | 1.54 sec: 1.22x slower                                                  |
| richards                  | 53.5 ms                                                  | 66.3 ms: 1.24x slower                                                   |
| 2to3                      | 306 ms                                                   | 380 ms: 1.24x slower                                                    |
| richards_super            | 60.3 ms                                                  | 75.3 ms: 1.25x slower                                                   |
| sqlglot_optimize          | 62.4 ms                                                  | 78.9 ms: 1.27x slower                                                   |
| sqlglot_transpile         | 1.73 ms                                                  | 2.21 ms: 1.28x slower                                                   |
| sqlglot_parse             | 1.38 ms                                                  | 1.77 ms: 1.28x slower                                                   |
| genshi_text               | 27.7 ms                                                  | 35.7 ms: 1.29x slower                                                   |
| nqueens                   | 98.7 ms                                                  | 128 ms: 1.30x slower                                                    |
| chaos                     | 68.8 ms                                                  | 92.1 ms: 1.34x slower                                                   |
| pprint_safe_repr          | 926 ms                                                   | 1.25 sec: 1.35x slower                                                  |
| sympy_expand              | 455 ms                                                   | 618 ms: 1.36x slower                                                    |
| genshi_xml                | 60.2 ms                                                  | 82.2 ms: 1.37x slower                                                   |
| docutils                  | 2.91 sec                                                 | 3.98 sec: 1.37x slower                                                  |
| pprint_pformat            | 1.90 sec                                                 | 2.60 sec: 1.37x slower                                                  |
| pylint                    | 343 ms                                                   | 473 ms: 1.38x slower                                                    |
| sympy_integrate           | 21.0 ms                                                  | 29.0 ms: 1.38x slower                                                   |
| sympy_str                 | 264 ms                                                   | 368 ms: 1.40x slower                                                    |
| hexiom                    | 7.13 ms                                                  | 10.2 ms: 1.44x slower                                                   |
| regex_compile             | 128 ms                                                   | 190 ms: 1.48x slower                                                    |
| sympy_sum                 | 143 ms                                                   | 216 ms: 1.50x slower                                                    |
| generators                | 37.8 ms                                                  | 57.4 ms: 1.52x slower                                                   |
| unpack_sequence           | 57.2 ns                                                  | 146 ns: 2.55x slower                                                    |
| Geometric mean            | (ref)                                                    | 1.10x slower                                                            |

Benchmark hidden because not significant (14): xml_etree_generate, async_tree_cpu_io_mixed, nbody, xml_etree_process, regex_v8, pidigits, pickle_dict, regex_effbot, json_loads, xml_etree_parse, python_startup_no_site, async_tree_cpu_io_mixed_tg, sqlite_synth, async_generators
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.10x