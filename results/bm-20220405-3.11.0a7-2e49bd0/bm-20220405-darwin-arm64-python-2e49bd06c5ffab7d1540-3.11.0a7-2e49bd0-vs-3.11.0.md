
# Results vs. 3.11.0

- fork: python
- ref: 2e49bd06c5ffab7d1540
- machine: darwin-arm64
- commit hash: 2e49bd0
- commit date: 2022-04-05
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 162 ms: 1.01x slower                                                  |
| chameleon      | 4.57 ms                                                | 4.55 ms: 1.01x faster                                                 |
| docutils       | 1.47 sec                                               | 1.46 sec: 1.01x faster                                                |
| html5lib       | 34.7 ms                                                | 33.8 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 53.0 ms                                                | 52.8 ms: 1.00x faster                                                 |
| pidigits       | 281 ms                                                 | 281 ms: 1.00x slower                                                  |
| nbody          | 65.5 ms                                                | 66.1 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.20 ms: 1.20x faster                                                 |
| regex_compile  | 76.7 ms                                                | 75.5 ms: 1.02x faster                                                 |
| regex_dna      | 152 ms                                                 | 171 ms: 1.13x slower                                                  |
| regex_v8       | 16.2 ms                                                | 19.8 ms: 1.22x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                 | 102 ms: 1.04x faster                                                  |
| xml_etree_iterparse  | 69.2 ms                                                | 67.3 ms: 1.03x faster                                                 |
| pickle_dict          | 17.9 us                                                | 17.6 us: 1.02x faster                                                 |
| xml_etree_generate   | 48.8 ms                                                | 48.2 ms: 1.01x faster                                                 |
| json_loads           | 16.1 us                                                | 15.9 us: 1.01x faster                                                 |
| unpickle_pure_python | 159 us                                                 | 157 us: 1.01x faster                                                  |
| json_dumps           | 7.72 ms                                                | 7.68 ms: 1.01x faster                                                 |
| unpickle_list        | 2.63 us                                                | 2.65 us: 1.01x slower                                                 |
| unpickle             | 9.70 us                                                | 9.87 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (4): pickle, xml_etree_process, pickle_pure_python, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 9.78 ms: 1.05x slower                                                 |
| python_startup         | 11.5 ms                                                | 12.1 ms: 1.05x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.49 ms                                                | 8.21 ms: 1.03x faster                                                 |
| genshi_text     | 15.3 ms                                                | 15.1 ms: 1.01x faster                                                 |
| django_template | 21.0 ms                                                | 21.2 ms: 1.01x slower                                                 |
| genshi_xml      | 29.8 ms                                                | 30.5 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot            | 2.63 ms                                                | 2.20 ms: 1.20x faster                                                 |
| unpack_sequence         | 33.6 ns                                                | 32.0 ns: 1.05x faster                                                 |
| dask                    | 226 ms                                                 | 217 ms: 1.05x faster                                                  |
| deltablue               | 2.81 ms                                                | 2.69 ms: 1.04x faster                                                 |
| xml_etree_parse         | 106 ms                                                 | 102 ms: 1.04x faster                                                  |
| sympy_sum               | 86.0 ms                                                | 82.6 ms: 1.04x faster                                                 |
| async_tree_memoization  | 336 ms                                                 | 323 ms: 1.04x faster                                                  |
| mako                    | 8.49 ms                                                | 8.21 ms: 1.03x faster                                                 |
| logging_format          | 3.78 us                                                | 3.65 us: 1.03x faster                                                 |
| xml_etree_iterparse     | 69.2 ms                                                | 67.3 ms: 1.03x faster                                                 |
| logging_simple          | 3.50 us                                                | 3.41 us: 1.03x faster                                                 |
| html5lib                | 34.7 ms                                                | 33.8 ms: 1.02x faster                                                 |
| sympy_str               | 152 ms                                                 | 148 ms: 1.02x faster                                                  |
| scimark_monte_carlo     | 46.4 ms                                                | 45.3 ms: 1.02x faster                                                 |
| sympy_integrate         | 11.5 ms                                                | 11.2 ms: 1.02x faster                                                 |
| coroutines              | 17.7 ms                                                | 17.3 ms: 1.02x faster                                                 |
| deepcopy_memo           | 26.3 us                                                | 25.8 us: 1.02x faster                                                 |
| generators              | 28.8 ms                                                | 28.3 ms: 1.02x faster                                                 |
| pprint_safe_repr        | 465 ms                                                 | 457 ms: 1.02x faster                                                  |
| regex_compile           | 76.7 ms                                                | 75.5 ms: 1.02x faster                                                 |
| pickle_dict             | 17.9 us                                                | 17.6 us: 1.02x faster                                                 |
| pprint_pformat          | 950 ms                                                 | 937 ms: 1.01x faster                                                  |
| xml_etree_generate      | 48.8 ms                                                | 48.2 ms: 1.01x faster                                                 |
| pathlib                 | 27.8 ms                                                | 27.5 ms: 1.01x faster                                                 |
| sympy_expand            | 243 ms                                                 | 241 ms: 1.01x faster                                                  |
| scimark_sor             | 83.0 ms                                                | 82.2 ms: 1.01x faster                                                 |
| json_loads              | 16.1 us                                                | 15.9 us: 1.01x faster                                                 |
| gc_traversal            | 2.43 ms                                                | 2.41 ms: 1.01x faster                                                 |
| docutils                | 1.47 sec                                               | 1.46 sec: 1.01x faster                                                |
| go                      | 109 ms                                                 | 108 ms: 1.01x faster                                                  |
| genshi_text             | 15.3 ms                                                | 15.1 ms: 1.01x faster                                                 |
| unpickle_pure_python    | 159 us                                                 | 157 us: 1.01x faster                                                  |
| async_generators        | 195 ms                                                 | 193 ms: 1.01x faster                                                  |
| chameleon               | 4.57 ms                                                | 4.55 ms: 1.01x faster                                                 |
| asyncio_tcp             | 651 ms                                                 | 648 ms: 1.01x faster                                                  |
| json_dumps              | 7.72 ms                                                | 7.68 ms: 1.01x faster                                                 |
| async_tree_none         | 285 ms                                                 | 283 ms: 1.00x faster                                                  |
| float                   | 53.0 ms                                                | 52.8 ms: 1.00x faster                                                 |
| async_tree_io           | 706 ms                                                 | 703 ms: 1.00x faster                                                  |
| thrift                  | 433 us                                                 | 432 us: 1.00x faster                                                  |
| create_gc_cycles        | 726 us                                                 | 724 us: 1.00x faster                                                  |
| pidigits                | 281 ms                                                 | 281 ms: 1.00x slower                                                  |
| scimark_lu              | 72.1 ms                                                | 72.2 ms: 1.00x slower                                                 |
| scimark_sparse_mat_mult | 3.20 ms                                                | 3.21 ms: 1.00x slower                                                 |
| chaos                   | 49.5 ms                                                | 49.7 ms: 1.00x slower                                                 |
| telco                   | 3.39 ms                                                | 3.41 ms: 1.01x slower                                                 |
| 2to3                    | 161 ms                                                 | 162 ms: 1.01x slower                                                  |
| fannkuch                | 261 ms                                                 | 262 ms: 1.01x slower                                                  |
| mdp                     | 1.54 sec                                               | 1.55 sec: 1.01x slower                                                |
| unpickle_list           | 2.63 us                                                | 2.65 us: 1.01x slower                                                 |
| sqlalchemy_imperative   | 7.31 ms                                                | 7.37 ms: 1.01x slower                                                 |
| django_template         | 21.0 ms                                                | 21.2 ms: 1.01x slower                                                 |
| nbody                   | 65.5 ms                                                | 66.1 ms: 1.01x slower                                                 |
| spectral_norm           | 72.8 ms                                                | 73.4 ms: 1.01x slower                                                 |
| deepcopy_reduce         | 1.91 us                                                | 1.93 us: 1.01x slower                                                 |
| sqlglot_normalize       | 171 ms                                                 | 173 ms: 1.01x slower                                                  |
| sqlalchemy_declarative  | 62.7 ms                                                | 63.3 ms: 1.01x slower                                                 |
| async_tree_cpu_io_mixed | 534 ms                                                 | 541 ms: 1.01x slower                                                  |
| meteor_contest          | 73.8 ms                                                | 74.7 ms: 1.01x slower                                                 |
| dulwich_log             | 29.9 ms                                                | 30.3 ms: 1.01x slower                                                 |
| richards                | 32.2 ms                                                | 32.6 ms: 1.01x slower                                                 |
| deepcopy                | 224 us                                                 | 227 us: 1.02x slower                                                  |
| pyflate                 | 311 ms                                                 | 316 ms: 1.02x slower                                                  |
| unpickle                | 9.70 us                                                | 9.87 us: 1.02x slower                                                 |
| json                    | 2.77 ms                                                | 2.82 ms: 1.02x slower                                                 |
| sqlglot_optimize        | 31.2 ms                                                | 31.9 ms: 1.02x slower                                                 |
| pylint                  | 271 ms                                                 | 277 ms: 1.02x slower                                                  |
| genshi_xml              | 29.8 ms                                                | 30.5 ms: 1.02x slower                                                 |
| logging_silent          | 68.0 ns                                                | 69.6 ns: 1.02x slower                                                 |
| raytrace                | 207 ms                                                 | 212 ms: 1.02x slower                                                  |
| pycparser               | 697 ms                                                 | 717 ms: 1.03x slower                                                  |
| hexiom                  | 4.73 ms                                                | 4.88 ms: 1.03x slower                                                 |
| python_startup_no_site  | 9.31 ms                                                | 9.78 ms: 1.05x slower                                                 |
| python_startup          | 11.5 ms                                                | 12.1 ms: 1.05x slower                                                 |
| bench_thread_pool       | 473 us                                                 | 499 us: 1.06x slower                                                  |
| comprehensions          | 16.1 us                                                | 17.5 us: 1.09x slower                                                 |
| crypto_pyaes            | 51.7 ms                                                | 56.5 ms: 1.09x slower                                                 |
| regex_dna               | 152 ms                                                 | 171 ms: 1.13x slower                                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.33 ms: 1.19x slower                                                 |
| sqlglot_parse           | 957 us                                                 | 1.17 ms: 1.22x slower                                                 |
| regex_v8                | 16.2 ms                                                | 19.8 ms: 1.22x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (13): nqueens, pickle, tornado_http, xml_etree_process, sqlite_synth, scimark_fft, bench_mp_pool, pickle_pure_python, pickle_list, mypy2, flaskblogging, gunicorn, aiohttp
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: coverage
