
# Results vs. 3.11.0

- fork: python
- ref: 3ddfa55df48a67a5972f
- machine: darwin-arm64
- commit hash: 3ddfa55
- commit date: 2022-03-07
- overall geometric mean: 1.02x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 185 ms: 1.15x slower                                                  |
| chameleon      | 4.57 ms                                                | 4.64 ms: 1.01x slower                                                 |
| docutils       | 1.47 sec                                               | 1.48 sec: 1.01x slower                                                |
| html5lib       | 34.7 ms                                                | 33.3 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                                  |
| nbody          | 65.5 ms                                                | 66.0 ms: 1.01x slower                                                 |
| float          | 53.0 ms                                                | 53.8 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.45 ms: 1.07x faster                                                 |
| regex_compile  | 76.7 ms                                                | 76.1 ms: 1.01x faster                                                 |
| regex_dna      | 152 ms                                                 | 162 ms: 1.07x slower                                                  |
| regex_v8       | 16.2 ms                                                | 18.2 ms: 1.12x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                 | 95.4 ms: 1.11x faster                                                 |
| xml_etree_iterparse  | 69.2 ms                                                | 64.8 ms: 1.07x faster                                                 |
| xml_etree_generate   | 48.8 ms                                                | 48.0 ms: 1.02x faster                                                 |
| json_dumps           | 7.72 ms                                                | 7.68 ms: 1.01x faster                                                 |
| pickle_list          | 2.81 us                                                | 2.83 us: 1.01x slower                                                 |
| pickle               | 7.17 us                                                | 7.24 us: 1.01x slower                                                 |
| xml_etree_process    | 35.2 ms                                                | 35.7 ms: 1.01x slower                                                 |
| pickle_dict          | 17.9 us                                                | 18.2 us: 1.02x slower                                                 |
| unpickle             | 9.70 us                                                | 9.95 us: 1.03x slower                                                 |
| pickle_pure_python   | 199 us                                                 | 205 us: 1.03x slower                                                  |
| unpickle_pure_python | 159 us                                                 | 169 us: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (2): unpickle_list, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 7.12 ms: 1.31x faster                                                 |
| python_startup         | 11.5 ms                                                | 12.9 ms: 1.12x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.49 ms                                                | 7.66 ms: 1.11x faster                                                 |
| genshi_text     | 15.3 ms                                                | 15.0 ms: 1.02x faster                                                 |
| django_template | 21.0 ms                                                | 22.2 ms: 1.06x slower                                                 |
| genshi_xml      | 29.8 ms                                                | 31.6 ms: 1.06x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pathlib                 | 27.8 ms                                                | 20.8 ms: 1.33x faster                                                 |
| python_startup_no_site  | 9.31 ms                                                | 7.12 ms: 1.31x faster                                                 |
| coverage                | 58.6 ms                                                | 50.4 ms: 1.16x faster                                                 |
| logging_simple          | 3.50 us                                                | 3.03 us: 1.16x faster                                                 |
| logging_format          | 3.78 us                                                | 3.31 us: 1.14x faster                                                 |
| xml_etree_parse         | 106 ms                                                 | 95.4 ms: 1.11x faster                                                 |
| mako                    | 8.49 ms                                                | 7.66 ms: 1.11x faster                                                 |
| regex_effbot            | 2.63 ms                                                | 2.45 ms: 1.07x faster                                                 |
| xml_etree_iterparse     | 69.2 ms                                                | 64.8 ms: 1.07x faster                                                 |
| aiohttp                 | 1.06 ms                                                | 1.01 ms: 1.05x faster                                                 |
| flaskblogging           | 2.42 ms                                                | 2.31 ms: 1.05x faster                                                 |
| html5lib                | 34.7 ms                                                | 33.3 ms: 1.04x faster                                                 |
| scimark_sor             | 83.0 ms                                                | 80.0 ms: 1.04x faster                                                 |
| chaos                   | 49.5 ms                                                | 48.2 ms: 1.03x faster                                                 |
| genshi_text             | 15.3 ms                                                | 15.0 ms: 1.02x faster                                                 |
| xml_etree_generate      | 48.8 ms                                                | 48.0 ms: 1.02x faster                                                 |
| hexiom                  | 4.73 ms                                                | 4.66 ms: 1.01x faster                                                 |
| sympy_sum               | 86.0 ms                                                | 84.9 ms: 1.01x faster                                                 |
| regex_compile           | 76.7 ms                                                | 76.1 ms: 1.01x faster                                                 |
| async_tree_io           | 706 ms                                                 | 701 ms: 1.01x faster                                                  |
| json_dumps              | 7.72 ms                                                | 7.68 ms: 1.01x faster                                                 |
| go                      | 109 ms                                                 | 109 ms: 1.00x faster                                                  |
| dulwich_log             | 29.9 ms                                                | 30.0 ms: 1.00x slower                                                 |
| pidigits                | 281 ms                                                 | 282 ms: 1.00x slower                                                  |
| sympy_str               | 152 ms                                                 | 152 ms: 1.00x slower                                                  |
| meteor_contest          | 73.8 ms                                                | 74.3 ms: 1.01x slower                                                 |
| sympy_integrate         | 11.5 ms                                                | 11.5 ms: 1.01x slower                                                 |
| async_tree_cpu_io_mixed | 534 ms                                                 | 538 ms: 1.01x slower                                                  |
| docutils                | 1.47 sec                                               | 1.48 sec: 1.01x slower                                                |
| nbody                   | 65.5 ms                                                | 66.0 ms: 1.01x slower                                                 |
| pickle_list             | 2.81 us                                                | 2.83 us: 1.01x slower                                                 |
| generators              | 28.8 ms                                                | 29.0 ms: 1.01x slower                                                 |
| pickle                  | 7.17 us                                                | 7.24 us: 1.01x slower                                                 |
| xml_etree_process       | 35.2 ms                                                | 35.7 ms: 1.01x slower                                                 |
| scimark_sparse_mat_mult | 3.20 ms                                                | 3.25 ms: 1.01x slower                                                 |
| chameleon               | 4.57 ms                                                | 4.64 ms: 1.01x slower                                                 |
| pickle_dict             | 17.9 us                                                | 18.2 us: 1.02x slower                                                 |
| float                   | 53.0 ms                                                | 53.8 ms: 1.02x slower                                                 |
| scimark_fft             | 199 ms                                                 | 203 ms: 1.02x slower                                                  |
| fannkuch                | 261 ms                                                 | 266 ms: 1.02x slower                                                  |
| json                    | 2.77 ms                                                | 2.83 ms: 1.02x slower                                                 |
| mdp                     | 1.54 sec                                               | 1.58 sec: 1.02x slower                                                |
| sqlite_synth            | 1.27 us                                                | 1.30 us: 1.02x slower                                                 |
| sqlglot_normalize       | 171 ms                                                 | 175 ms: 1.02x slower                                                  |
| sqlalchemy_imperative   | 7.31 ms                                                | 7.49 ms: 1.02x slower                                                 |
| unpickle                | 9.70 us                                                | 9.95 us: 1.03x slower                                                 |
| sqlalchemy_declarative  | 62.7 ms                                                | 64.4 ms: 1.03x slower                                                 |
| sympy_expand            | 243 ms                                                 | 250 ms: 1.03x slower                                                  |
| thrift                  | 433 us                                                 | 446 us: 1.03x slower                                                  |
| pickle_pure_python      | 199 us                                                 | 205 us: 1.03x slower                                                  |
| telco                   | 3.39 ms                                                | 3.51 ms: 1.03x slower                                                 |
| bench_mp_pool           | 43.2 ms                                                | 44.8 ms: 1.04x slower                                                 |
| scimark_lu              | 72.1 ms                                                | 74.7 ms: 1.04x slower                                                 |
| richards                | 32.2 ms                                                | 33.4 ms: 1.04x slower                                                 |
| deepcopy                | 224 us                                                 | 232 us: 1.04x slower                                                  |
| deepcopy_memo           | 26.3 us                                                | 27.4 us: 1.04x slower                                                 |
| pyflate                 | 311 ms                                                 | 325 ms: 1.04x slower                                                  |
| raytrace                | 207 ms                                                 | 216 ms: 1.04x slower                                                  |
| bench_thread_pool       | 473 us                                                 | 495 us: 1.05x slower                                                  |
| pprint_pformat          | 950 ms                                                 | 998 ms: 1.05x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                | 2.01 us: 1.05x slower                                                 |
| spectral_norm           | 72.8 ms                                                | 76.6 ms: 1.05x slower                                                 |
| pprint_safe_repr        | 465 ms                                                 | 490 ms: 1.05x slower                                                  |
| sqlglot_optimize        | 31.2 ms                                                | 32.9 ms: 1.05x slower                                                 |
| django_template         | 21.0 ms                                                | 22.2 ms: 1.06x slower                                                 |
| coroutines              | 17.7 ms                                                | 18.7 ms: 1.06x slower                                                 |
| deltablue               | 2.81 ms                                                | 2.97 ms: 1.06x slower                                                 |
| genshi_xml              | 29.8 ms                                                | 31.6 ms: 1.06x slower                                                 |
| pycparser               | 697 ms                                                 | 739 ms: 1.06x slower                                                  |
| unpickle_pure_python    | 159 us                                                 | 169 us: 1.06x slower                                                  |
| regex_dna               | 152 ms                                                 | 162 ms: 1.07x slower                                                  |
| logging_silent          | 68.0 ns                                                | 73.9 ns: 1.09x slower                                                 |
| scimark_monte_carlo     | 46.4 ms                                                | 51.3 ms: 1.11x slower                                                 |
| crypto_pyaes            | 51.7 ms                                                | 57.2 ms: 1.11x slower                                                 |
| async_tree_memoization  | 336 ms                                                 | 376 ms: 1.12x slower                                                  |
| python_startup          | 11.5 ms                                                | 12.9 ms: 1.12x slower                                                 |
| regex_v8                | 16.2 ms                                                | 18.2 ms: 1.12x slower                                                 |
| 2to3                    | 161 ms                                                 | 185 ms: 1.15x slower                                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.35 ms: 1.21x slower                                                 |
| sqlglot_parse           | 957 us                                                 | 1.18 ms: 1.23x slower                                                 |
| unpack_sequence         | 33.6 ns                                                | 90.4 ns: 2.69x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (8): gunicorn, nqueens, async_tree_none, unpickle_list, async_generators, json_loads, pylint, tornado_http
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp, comprehensions, create_gc_cycles, dask, gc_traversal, mypy2
