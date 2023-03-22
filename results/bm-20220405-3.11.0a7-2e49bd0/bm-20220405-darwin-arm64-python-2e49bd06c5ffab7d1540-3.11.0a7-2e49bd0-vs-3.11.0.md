
# Results vs. 3.11.0

- fork: python
- ref: 2e49bd06c5ffab7d1540
- machine: darwin-arm64
- commit hash: 2e49bd0
- commit date: 2022-04-05
- overall geometric mean: 1.01x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 181 ms: 1.13x slower                                                  |
| chameleon      | 4.57 ms                                                | 4.70 ms: 1.03x slower                                                 |
| docutils       | 1.47 sec                                               | 1.45 sec: 1.01x faster                                                |
| html5lib       | 34.7 ms                                                | 34.0 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 53.0 ms                                                | 51.6 ms: 1.03x faster                                                 |
| pidigits       | 281 ms                                                 | 282 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.20 ms: 1.20x faster                                                 |
| regex_compile  | 76.7 ms                                                | 75.6 ms: 1.01x faster                                                 |
| regex_dna      | 152 ms                                                 | 169 ms: 1.12x slower                                                  |
| regex_v8       | 16.2 ms                                                | 20.5 ms: 1.26x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                 | 95.7 ms: 1.11x faster                                                 |
| xml_etree_iterparse  | 69.2 ms                                                | 64.4 ms: 1.08x faster                                                 |
| xml_etree_generate   | 48.8 ms                                                | 47.9 ms: 1.02x faster                                                 |
| json_dumps           | 7.72 ms                                                | 7.58 ms: 1.02x faster                                                 |
| unpickle_pure_python | 159 us                                                 | 157 us: 1.01x faster                                                  |
| xml_etree_process    | 35.2 ms                                                | 35.1 ms: 1.00x faster                                                 |
| unpickle_list        | 2.63 us                                                | 2.62 us: 1.00x faster                                                 |
| pickle_pure_python   | 199 us                                                 | 200 us: 1.00x slower                                                  |
| json_loads           | 16.1 us                                                | 16.3 us: 1.01x slower                                                 |
| unpickle             | 9.70 us                                                | 9.82 us: 1.01x slower                                                 |
| pickle_dict          | 17.9 us                                                | 19.2 us: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (2): pickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 7.18 ms: 1.30x faster                                                 |
| python_startup         | 11.5 ms                                                | 9.13 ms: 1.26x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.28x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.49 ms                                                | 8.21 ms: 1.03x faster                                                 |
| genshi_text     | 15.3 ms                                                | 15.2 ms: 1.00x faster                                                 |
| django_template | 21.0 ms                                                | 21.1 ms: 1.01x slower                                                 |
| genshi_xml      | 29.8 ms                                                | 31.4 ms: 1.06x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pathlib                 | 27.8 ms                                                | 20.9 ms: 1.33x faster                                                 |
| python_startup_no_site  | 9.31 ms                                                | 7.18 ms: 1.30x faster                                                 |
| python_startup          | 11.5 ms                                                | 9.13 ms: 1.26x faster                                                 |
| regex_effbot            | 2.63 ms                                                | 2.20 ms: 1.20x faster                                                 |
| bench_mp_pool           | 43.2 ms                                                | 37.1 ms: 1.16x faster                                                 |
| xml_etree_parse         | 106 ms                                                 | 95.7 ms: 1.11x faster                                                 |
| xml_etree_iterparse     | 69.2 ms                                                | 64.4 ms: 1.08x faster                                                 |
| async_tree_memoization  | 336 ms                                                 | 316 ms: 1.06x faster                                                  |
| sympy_sum               | 86.0 ms                                                | 81.7 ms: 1.05x faster                                                 |
| deltablue               | 2.81 ms                                                | 2.67 ms: 1.05x faster                                                 |
| unpack_sequence         | 33.6 ns                                                | 31.9 ns: 1.05x faster                                                 |
| flaskblogging           | 2.42 ms                                                | 2.30 ms: 1.05x faster                                                 |
| logging_format          | 3.78 us                                                | 3.65 us: 1.04x faster                                                 |
| deepcopy_memo           | 26.3 us                                                | 25.4 us: 1.04x faster                                                 |
| logging_simple          | 3.50 us                                                | 3.38 us: 1.04x faster                                                 |
| mako                    | 8.49 ms                                                | 8.21 ms: 1.03x faster                                                 |
| generators              | 28.8 ms                                                | 27.9 ms: 1.03x faster                                                 |
| sympy_str               | 152 ms                                                 | 147 ms: 1.03x faster                                                  |
| float                   | 53.0 ms                                                | 51.6 ms: 1.03x faster                                                 |
| coroutines              | 17.7 ms                                                | 17.3 ms: 1.03x faster                                                 |
| sympy_integrate         | 11.5 ms                                                | 11.2 ms: 1.02x faster                                                 |
| async_generators        | 195 ms                                                 | 191 ms: 1.02x faster                                                  |
| nqueens                 | 61.8 ms                                                | 60.6 ms: 1.02x faster                                                 |
| html5lib                | 34.7 ms                                                | 34.0 ms: 1.02x faster                                                 |
| xml_etree_generate      | 48.8 ms                                                | 47.9 ms: 1.02x faster                                                 |
| async_tree_io           | 706 ms                                                 | 693 ms: 1.02x faster                                                  |
| json_dumps              | 7.72 ms                                                | 7.58 ms: 1.02x faster                                                 |
| dulwich_log             | 29.9 ms                                                | 29.4 ms: 1.02x faster                                                 |
| deepcopy                | 224 us                                                 | 220 us: 1.02x faster                                                  |
| async_tree_none         | 285 ms                                                 | 280 ms: 1.02x faster                                                  |
| regex_compile           | 76.7 ms                                                | 75.6 ms: 1.01x faster                                                 |
| go                      | 109 ms                                                 | 107 ms: 1.01x faster                                                  |
| docutils                | 1.47 sec                                               | 1.45 sec: 1.01x faster                                                |
| pprint_safe_repr        | 465 ms                                                 | 460 ms: 1.01x faster                                                  |
| pprint_pformat          | 950 ms                                                 | 940 ms: 1.01x faster                                                  |
| sympy_expand            | 243 ms                                                 | 241 ms: 1.01x faster                                                  |
| unpickle_pure_python    | 159 us                                                 | 157 us: 1.01x faster                                                  |
| xml_etree_process       | 35.2 ms                                                | 35.1 ms: 1.00x faster                                                 |
| unpickle_list           | 2.63 us                                                | 2.62 us: 1.00x faster                                                 |
| genshi_text             | 15.3 ms                                                | 15.2 ms: 1.00x faster                                                 |
| fannkuch                | 261 ms                                                 | 262 ms: 1.00x slower                                                  |
| pickle_pure_python      | 199 us                                                 | 200 us: 1.00x slower                                                  |
| chaos                   | 49.5 ms                                                | 49.7 ms: 1.01x slower                                                 |
| django_template         | 21.0 ms                                                | 21.1 ms: 1.01x slower                                                 |
| pidigits                | 281 ms                                                 | 282 ms: 1.01x slower                                                  |
| sqlglot_normalize       | 171 ms                                                 | 172 ms: 1.01x slower                                                  |
| scimark_sparse_mat_mult | 3.20 ms                                                | 3.22 ms: 1.01x slower                                                 |
| scimark_fft             | 199 ms                                                 | 201 ms: 1.01x slower                                                  |
| bench_thread_pool       | 473 us                                                 | 476 us: 1.01x slower                                                  |
| sqlalchemy_imperative   | 7.31 ms                                                | 7.37 ms: 1.01x slower                                                 |
| scimark_lu              | 72.1 ms                                                | 72.6 ms: 1.01x slower                                                 |
| sqlalchemy_declarative  | 62.7 ms                                                | 63.2 ms: 1.01x slower                                                 |
| raytrace                | 207 ms                                                 | 209 ms: 1.01x slower                                                  |
| scimark_monte_carlo     | 46.4 ms                                                | 46.9 ms: 1.01x slower                                                 |
| spectral_norm           | 72.8 ms                                                | 73.6 ms: 1.01x slower                                                 |
| json_loads              | 16.1 us                                                | 16.3 us: 1.01x slower                                                 |
| thrift                  | 433 us                                                 | 439 us: 1.01x slower                                                  |
| sqlite_synth            | 1.27 us                                                | 1.29 us: 1.01x slower                                                 |
| unpickle                | 9.70 us                                                | 9.82 us: 1.01x slower                                                 |
| pyflate                 | 311 ms                                                 | 317 ms: 1.02x slower                                                  |
| meteor_contest          | 73.8 ms                                                | 75.2 ms: 1.02x slower                                                 |
| scimark_sor             | 83.0 ms                                                | 84.7 ms: 1.02x slower                                                 |
| logging_silent          | 68.0 ns                                                | 69.4 ns: 1.02x slower                                                 |
| sqlglot_optimize        | 31.2 ms                                                | 31.9 ms: 1.02x slower                                                 |
| chameleon               | 4.57 ms                                                | 4.70 ms: 1.03x slower                                                 |
| hexiom                  | 4.73 ms                                                | 4.87 ms: 1.03x slower                                                 |
| pycparser               | 697 ms                                                 | 721 ms: 1.03x slower                                                  |
| json                    | 2.77 ms                                                | 2.92 ms: 1.05x slower                                                 |
| genshi_xml              | 29.8 ms                                                | 31.4 ms: 1.06x slower                                                 |
| pickle_dict             | 17.9 us                                                | 19.2 us: 1.08x slower                                                 |
| mdp                     | 1.54 sec                                               | 1.66 sec: 1.08x slower                                                |
| crypto_pyaes            | 51.7 ms                                                | 56.5 ms: 1.09x slower                                                 |
| regex_dna               | 152 ms                                                 | 169 ms: 1.12x slower                                                  |
| 2to3                    | 161 ms                                                 | 181 ms: 1.13x slower                                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.33 ms: 1.19x slower                                                 |
| sqlglot_parse           | 957 us                                                 | 1.17 ms: 1.22x slower                                                 |
| regex_v8                | 16.2 ms                                                | 20.5 ms: 1.26x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (11): tornado_http, gunicorn, aiohttp, pickle_list, richards, async_tree_cpu_io_mixed, telco, deepcopy_reduce, pylint, nbody, pickle
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp, comprehensions, coverage, create_gc_cycles, dask, gc_traversal, mypy2
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220405-3.11.0a7-2e49bd0/bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0.json: mypy
