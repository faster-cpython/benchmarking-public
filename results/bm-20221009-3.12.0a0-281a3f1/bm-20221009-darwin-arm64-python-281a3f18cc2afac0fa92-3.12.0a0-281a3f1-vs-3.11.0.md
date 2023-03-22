
# Results vs. 3.11.0

- fork: python
- ref: 281a3f18cc2afac0fa92
- machine: darwin-arm64
- commit hash: 281a3f1
- commit date: 2022-10-09
- overall geometric mean: 1.00x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221009-darwin-arm64-python-281a3f18cc2afac0fa92-3.12.0a0-281a3f1 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 186 ms: 1.15x slower                                                  |
| chameleon      | 4.57 ms                                                | 4.61 ms: 1.01x slower                                                 |
| html5lib       | 34.7 ms                                                | 36.6 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221009-darwin-arm64-python-281a3f18cc2afac0fa92-3.12.0a0-281a3f1 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 65.5 ms                                                | 64.3 ms: 1.02x faster                                                 |
| pidigits       | 281 ms                                                 | 282 ms: 1.01x slower                                                  |
| float          | 53.0 ms                                                | 56.1 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221009-darwin-arm64-python-281a3f18cc2afac0fa92-3.12.0a0-281a3f1 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 76.5 ms: 1.00x faster                                                 |
| regex_v8       | 16.2 ms                                                | 16.3 ms: 1.01x slower                                                 |
| regex_effbot   | 2.63 ms                                                | 2.68 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221009-darwin-arm64-python-281a3f18cc2afac0fa92-3.12.0a0-281a3f1 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 7.72 ms                                                | 6.17 ms: 1.25x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 90.0 ms: 1.18x faster                                                 |
| xml_etree_iterparse  | 69.2 ms                                                | 64.6 ms: 1.07x faster                                                 |
| xml_etree_generate   | 48.8 ms                                                | 47.1 ms: 1.04x faster                                                 |
| unpickle_list        | 2.63 us                                                | 2.54 us: 1.04x faster                                                 |
| xml_etree_process    | 35.2 ms                                                | 34.9 ms: 1.01x faster                                                 |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.01x slower                                                 |
| json_loads           | 16.1 us                                                | 16.3 us: 1.01x slower                                                 |
| unpickle_pure_python | 159 us                                                 | 162 us: 1.02x slower                                                  |
| pickle_list          | 2.81 us                                                | 2.91 us: 1.04x slower                                                 |
| pickle_pure_python   | 199 us                                                 | 208 us: 1.05x slower                                                  |
| pickle               | 7.17 us                                                | 7.56 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221009-darwin-arm64-python-281a3f18cc2afac0fa92-3.12.0a0-281a3f1 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 7.41 ms: 1.26x faster                                                 |
| python_startup         | 11.5 ms                                                | 9.38 ms: 1.23x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221009-darwin-arm64-python-281a3f18cc2afac0fa92-3.12.0a0-281a3f1 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.49 ms                                                | 8.11 ms: 1.05x faster                                                 |
| genshi_text     | 15.3 ms                                                | 15.3 ms: 1.00x slower                                                 |
| genshi_xml      | 29.8 ms                                                | 30.1 ms: 1.01x slower                                                 |
| django_template | 21.0 ms                                                | 21.7 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221009-darwin-arm64-python-281a3f18cc2afac0fa92-3.12.0a0-281a3f1 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pathlib                 | 27.8 ms                                                | 20.8 ms: 1.34x faster                                                 |
| python_startup_no_site  | 9.31 ms                                                | 7.41 ms: 1.26x faster                                                 |
| json_dumps              | 7.72 ms                                                | 6.17 ms: 1.25x faster                                                 |
| python_startup          | 11.5 ms                                                | 9.38 ms: 1.23x faster                                                 |
| xml_etree_parse         | 106 ms                                                 | 90.0 ms: 1.18x faster                                                 |
| scimark_sparse_mat_mult | 3.20 ms                                                | 2.78 ms: 1.15x faster                                                 |
| coverage                | 58.6 ms                                                | 53.4 ms: 1.10x faster                                                 |
| xml_etree_iterparse     | 69.2 ms                                                | 64.6 ms: 1.07x faster                                                 |
| mako                    | 8.49 ms                                                | 8.11 ms: 1.05x faster                                                 |
| bench_thread_pool       | 473 us                                                 | 452 us: 1.04x faster                                                  |
| bench_mp_pool           | 43.2 ms                                                | 41.4 ms: 1.04x faster                                                 |
| xml_etree_generate      | 48.8 ms                                                | 47.1 ms: 1.04x faster                                                 |
| unpickle_list           | 2.63 us                                                | 2.54 us: 1.04x faster                                                 |
| logging_silent          | 68.0 ns                                                | 65.9 ns: 1.03x faster                                                 |
| async_tree_memoization  | 336 ms                                                 | 325 ms: 1.03x faster                                                  |
| sqlalchemy_declarative  | 62.7 ms                                                | 61.0 ms: 1.03x faster                                                 |
| deltablue               | 2.81 ms                                                | 2.74 ms: 1.02x faster                                                 |
| nqueens                 | 61.8 ms                                                | 60.3 ms: 1.02x faster                                                 |
| telco                   | 3.39 ms                                                | 3.32 ms: 1.02x faster                                                 |
| sqlalchemy_imperative   | 7.31 ms                                                | 7.16 ms: 1.02x faster                                                 |
| nbody                   | 65.5 ms                                                | 64.3 ms: 1.02x faster                                                 |
| dulwich_log             | 29.9 ms                                                | 29.3 ms: 1.02x faster                                                 |
| mdp                     | 1.54 sec                                               | 1.52 sec: 1.01x faster                                                |
| xml_etree_process       | 35.2 ms                                                | 34.9 ms: 1.01x faster                                                 |
| spectral_norm           | 72.8 ms                                                | 72.5 ms: 1.00x faster                                                 |
| regex_compile           | 76.7 ms                                                | 76.5 ms: 1.00x faster                                                 |
| unpack_sequence         | 33.6 ns                                                | 33.5 ns: 1.00x faster                                                 |
| crypto_pyaes            | 51.7 ms                                                | 51.8 ms: 1.00x slower                                                 |
| genshi_text             | 15.3 ms                                                | 15.3 ms: 1.00x slower                                                 |
| sympy_str               | 152 ms                                                 | 153 ms: 1.01x slower                                                  |
| pidigits                | 281 ms                                                 | 282 ms: 1.01x slower                                                  |
| generators              | 28.8 ms                                                | 29.0 ms: 1.01x slower                                                 |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.01x slower                                                 |
| regex_v8                | 16.2 ms                                                | 16.3 ms: 1.01x slower                                                 |
| async_tree_none         | 285 ms                                                 | 287 ms: 1.01x slower                                                  |
| chameleon               | 4.57 ms                                                | 4.61 ms: 1.01x slower                                                 |
| thrift                  | 433 us                                                 | 438 us: 1.01x slower                                                  |
| sqlglot_normalize       | 171 ms                                                 | 173 ms: 1.01x slower                                                  |
| sympy_expand            | 243 ms                                                 | 246 ms: 1.01x slower                                                  |
| genshi_xml              | 29.8 ms                                                | 30.1 ms: 1.01x slower                                                 |
| sympy_integrate         | 11.5 ms                                                | 11.6 ms: 1.01x slower                                                 |
| json_loads              | 16.1 us                                                | 16.3 us: 1.01x slower                                                 |
| pycparser               | 697 ms                                                 | 706 ms: 1.01x slower                                                  |
| regex_effbot            | 2.63 ms                                                | 2.68 ms: 1.02x slower                                                 |
| sqlglot_optimize        | 31.2 ms                                                | 31.7 ms: 1.02x slower                                                 |
| chaos                   | 49.5 ms                                                | 50.4 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed | 534 ms                                                 | 545 ms: 1.02x slower                                                  |
| unpickle_pure_python    | 159 us                                                 | 162 us: 1.02x slower                                                  |
| async_generators        | 195 ms                                                 | 199 ms: 1.02x slower                                                  |
| scimark_lu              | 72.1 ms                                                | 73.9 ms: 1.02x slower                                                 |
| json                    | 2.77 ms                                                | 2.84 ms: 1.03x slower                                                 |
| fannkuch                | 261 ms                                                 | 269 ms: 1.03x slower                                                  |
| meteor_contest          | 73.8 ms                                                | 76.2 ms: 1.03x slower                                                 |
| django_template         | 21.0 ms                                                | 21.7 ms: 1.03x slower                                                 |
| pickle_list             | 2.81 us                                                | 2.91 us: 1.04x slower                                                 |
| richards                | 32.2 ms                                                | 33.5 ms: 1.04x slower                                                 |
| hexiom                  | 4.73 ms                                                | 4.92 ms: 1.04x slower                                                 |
| async_tree_io           | 706 ms                                                 | 736 ms: 1.04x slower                                                  |
| pprint_pformat          | 950 ms                                                 | 992 ms: 1.04x slower                                                  |
| logging_simple          | 3.50 us                                                | 3.66 us: 1.04x slower                                                 |
| pprint_safe_repr        | 465 ms                                                 | 486 ms: 1.05x slower                                                  |
| pickle_pure_python      | 199 us                                                 | 208 us: 1.05x slower                                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.18 ms: 1.05x slower                                                 |
| sqlglot_parse           | 957 us                                                 | 1.01 ms: 1.05x slower                                                 |
| pickle                  | 7.17 us                                                | 7.56 us: 1.05x slower                                                 |
| raytrace                | 207 ms                                                 | 219 ms: 1.06x slower                                                  |
| html5lib                | 34.7 ms                                                | 36.6 ms: 1.06x slower                                                 |
| logging_format          | 3.78 us                                                | 4.00 us: 1.06x slower                                                 |
| float                   | 53.0 ms                                                | 56.1 ms: 1.06x slower                                                 |
| deepcopy                | 224 us                                                 | 239 us: 1.07x slower                                                  |
| coroutines              | 17.7 ms                                                | 19.0 ms: 1.07x slower                                                 |
| deepcopy_reduce         | 1.91 us                                                | 2.06 us: 1.08x slower                                                 |
| go                      | 109 ms                                                 | 120 ms: 1.10x slower                                                  |
| deepcopy_memo           | 26.3 us                                                | 29.2 us: 1.11x slower                                                 |
| pyflate                 | 311 ms                                                 | 352 ms: 1.13x slower                                                  |
| sqlite_synth            | 1.27 us                                                | 1.45 us: 1.14x slower                                                 |
| 2to3                    | 161 ms                                                 | 186 ms: 1.15x slower                                                  |
| scimark_monte_carlo     | 46.4 ms                                                | 54.6 ms: 1.18x slower                                                 |
| scimark_sor             | 83.0 ms                                                | 101 ms: 1.22x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (7): tornado_http, pylint, scimark_fft, regex_dna, sympy_sum, docutils, unpickle
Ignored benchmarks (9) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221009-3.12.0a0-281a3f1/bm-20221009-darwin-arm64-python-281a3f18cc2afac0fa92-3.12.0a0-281a3f1.json: mypy
