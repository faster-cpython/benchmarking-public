
# Results vs. 3.11.0

- fork: python
- ref: 3ddfa55df48a67a5972f
- machine: darwin-arm64
- commit hash: 3ddfa55
- commit date: 2022-03-07
- overall geometric mean: 1.03x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 165 ms: 1.03x slower                                                  |
| chameleon      | 4.57 ms                                                | 4.60 ms: 1.01x slower                                                 |
| docutils       | 1.47 sec                                               | 1.49 sec: 1.01x slower                                                |
| html5lib       | 34.7 ms                                                | 33.4 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 281 ms                                                 | 281 ms: 1.00x slower                                                  |
| nbody          | 65.5 ms                                                | 66.5 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.45 ms: 1.08x faster                                                 |
| regex_compile  | 76.7 ms                                                | 76.2 ms: 1.01x faster                                                 |
| regex_dna      | 152 ms                                                 | 162 ms: 1.07x slower                                                  |
| regex_v8       | 16.2 ms                                                | 17.8 ms: 1.10x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                 | 102 ms: 1.04x faster                                                  |
| pickle_dict          | 17.9 us                                                | 17.5 us: 1.02x faster                                                 |
| xml_etree_iterparse  | 69.2 ms                                                | 68.3 ms: 1.01x faster                                                 |
| xml_etree_generate   | 48.8 ms                                                | 48.2 ms: 1.01x faster                                                 |
| json_dumps           | 7.72 ms                                                | 7.65 ms: 1.01x faster                                                 |
| json_loads           | 16.1 us                                                | 16.0 us: 1.01x faster                                                 |
| pickle               | 7.17 us                                                | 7.15 us: 1.00x faster                                                 |
| pickle_list          | 2.81 us                                                | 2.85 us: 1.01x slower                                                 |
| unpickle             | 9.70 us                                                | 9.85 us: 1.02x slower                                                 |
| xml_etree_process    | 35.2 ms                                                | 36.1 ms: 1.03x slower                                                 |
| pickle_pure_python   | 199 us                                                 | 204 us: 1.03x slower                                                  |
| unpickle_pure_python | 159 us                                                 | 168 us: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 9.77 ms: 1.05x slower                                                 |
| python_startup         | 11.5 ms                                                | 15.6 ms: 1.35x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.19x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.49 ms                                                | 7.66 ms: 1.11x faster                                                 |
| genshi_text     | 15.3 ms                                                | 15.1 ms: 1.01x faster                                                 |
| genshi_xml      | 29.8 ms                                                | 31.2 ms: 1.05x slower                                                 |
| django_template | 21.0 ms                                                | 22.2 ms: 1.06x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coverage                | 58.6 ms                                                | 50.9 ms: 1.15x faster                                                 |
| logging_simple          | 3.50 us                                                | 3.08 us: 1.14x faster                                                 |
| logging_format          | 3.78 us                                                | 3.36 us: 1.12x faster                                                 |
| mako                    | 8.49 ms                                                | 7.66 ms: 1.11x faster                                                 |
| regex_effbot            | 2.63 ms                                                | 2.45 ms: 1.08x faster                                                 |
| xml_etree_parse         | 106 ms                                                 | 102 ms: 1.04x faster                                                  |
| pathlib                 | 27.8 ms                                                | 26.7 ms: 1.04x faster                                                 |
| html5lib                | 34.7 ms                                                | 33.4 ms: 1.04x faster                                                 |
| scimark_sor             | 83.0 ms                                                | 80.0 ms: 1.04x faster                                                 |
| chaos                   | 49.5 ms                                                | 48.1 ms: 1.03x faster                                                 |
| pickle_dict             | 17.9 us                                                | 17.5 us: 1.02x faster                                                 |
| hexiom                  | 4.73 ms                                                | 4.67 ms: 1.01x faster                                                 |
| xml_etree_iterparse     | 69.2 ms                                                | 68.3 ms: 1.01x faster                                                 |
| xml_etree_generate      | 48.8 ms                                                | 48.2 ms: 1.01x faster                                                 |
| sympy_sum               | 86.0 ms                                                | 85.3 ms: 1.01x faster                                                 |
| json_dumps              | 7.72 ms                                                | 7.65 ms: 1.01x faster                                                 |
| genshi_text             | 15.3 ms                                                | 15.1 ms: 1.01x faster                                                 |
| go                      | 109 ms                                                 | 108 ms: 1.01x faster                                                  |
| regex_compile           | 76.7 ms                                                | 76.2 ms: 1.01x faster                                                 |
| json_loads              | 16.1 us                                                | 16.0 us: 1.01x faster                                                 |
| gc_traversal            | 2.43 ms                                                | 2.43 ms: 1.00x faster                                                 |
| pickle                  | 7.17 us                                                | 7.15 us: 1.00x faster                                                 |
| pidigits                | 281 ms                                                 | 281 ms: 1.00x slower                                                  |
| async_generators        | 195 ms                                                 | 195 ms: 1.00x slower                                                  |
| create_gc_cycles        | 726 us                                                 | 729 us: 1.00x slower                                                  |
| chameleon               | 4.57 ms                                                | 4.60 ms: 1.01x slower                                                 |
| async_tree_io           | 706 ms                                                 | 711 ms: 1.01x slower                                                  |
| sympy_str               | 152 ms                                                 | 153 ms: 1.01x slower                                                  |
| async_tree_none         | 285 ms                                                 | 288 ms: 1.01x slower                                                  |
| docutils                | 1.47 sec                                               | 1.49 sec: 1.01x slower                                                |
| json                    | 2.77 ms                                                | 2.80 ms: 1.01x slower                                                 |
| generators              | 28.8 ms                                                | 29.2 ms: 1.01x slower                                                 |
| pickle_list             | 2.81 us                                                | 2.85 us: 1.01x slower                                                 |
| async_tree_cpu_io_mixed | 534 ms                                                 | 542 ms: 1.01x slower                                                  |
| fannkuch                | 261 ms                                                 | 265 ms: 1.02x slower                                                  |
| unpickle                | 9.70 us                                                | 9.85 us: 1.02x slower                                                 |
| sympy_integrate         | 11.5 ms                                                | 11.7 ms: 1.02x slower                                                 |
| nbody                   | 65.5 ms                                                | 66.5 ms: 1.02x slower                                                 |
| scimark_fft             | 199 ms                                                 | 203 ms: 1.02x slower                                                  |
| scimark_sparse_mat_mult | 3.20 ms                                                | 3.26 ms: 1.02x slower                                                 |
| meteor_contest          | 73.8 ms                                                | 75.2 ms: 1.02x slower                                                 |
| sqlite_synth            | 1.27 us                                                | 1.30 us: 1.02x slower                                                 |
| thrift                  | 433 us                                                 | 443 us: 1.02x slower                                                  |
| flaskblogging           | 2.42 ms                                                | 2.48 ms: 1.02x slower                                                 |
| xml_etree_process       | 35.2 ms                                                | 36.1 ms: 1.03x slower                                                 |
| 2to3                    | 161 ms                                                 | 165 ms: 1.03x slower                                                  |
| sqlglot_normalize       | 171 ms                                                 | 176 ms: 1.03x slower                                                  |
| mdp                     | 1.54 sec                                               | 1.58 sec: 1.03x slower                                                |
| pickle_pure_python      | 199 us                                                 | 204 us: 1.03x slower                                                  |
| richards                | 32.2 ms                                                | 33.1 ms: 1.03x slower                                                 |
| bench_mp_pool           | 43.2 ms                                                | 44.5 ms: 1.03x slower                                                 |
| scimark_lu              | 72.1 ms                                                | 74.4 ms: 1.03x slower                                                 |
| raytrace                | 207 ms                                                 | 214 ms: 1.03x slower                                                  |
| sqlalchemy_imperative   | 7.31 ms                                                | 7.57 ms: 1.04x slower                                                 |
| deepcopy                | 224 us                                                 | 232 us: 1.04x slower                                                  |
| pyflate                 | 311 ms                                                 | 322 ms: 1.04x slower                                                  |
| sympy_expand            | 243 ms                                                 | 253 ms: 1.04x slower                                                  |
| sqlalchemy_declarative  | 62.7 ms                                                | 65.2 ms: 1.04x slower                                                 |
| dulwich_log             | 29.9 ms                                                | 31.1 ms: 1.04x slower                                                 |
| deepcopy_memo           | 26.3 us                                                | 27.4 us: 1.04x slower                                                 |
| pylint                  | 271 ms                                                 | 283 ms: 1.05x slower                                                  |
| genshi_xml              | 29.8 ms                                                | 31.2 ms: 1.05x slower                                                 |
| python_startup_no_site  | 9.31 ms                                                | 9.77 ms: 1.05x slower                                                 |
| telco                   | 3.39 ms                                                | 3.57 ms: 1.05x slower                                                 |
| pprint_pformat          | 950 ms                                                 | 999 ms: 1.05x slower                                                  |
| pprint_safe_repr        | 465 ms                                                 | 489 ms: 1.05x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                | 2.01 us: 1.05x slower                                                 |
| spectral_norm           | 72.8 ms                                                | 76.8 ms: 1.05x slower                                                 |
| sqlglot_optimize        | 31.2 ms                                                | 32.9 ms: 1.06x slower                                                 |
| django_template         | 21.0 ms                                                | 22.2 ms: 1.06x slower                                                 |
| coroutines              | 17.7 ms                                                | 18.7 ms: 1.06x slower                                                 |
| deltablue               | 2.81 ms                                                | 2.97 ms: 1.06x slower                                                 |
| pycparser               | 697 ms                                                 | 737 ms: 1.06x slower                                                  |
| unpickle_pure_python    | 159 us                                                 | 168 us: 1.06x slower                                                  |
| regex_dna               | 152 ms                                                 | 162 ms: 1.07x slower                                                  |
| bench_thread_pool       | 473 us                                                 | 513 us: 1.09x slower                                                  |
| logging_silent          | 68.0 ns                                                | 74.5 ns: 1.10x slower                                                 |
| regex_v8                | 16.2 ms                                                | 17.8 ms: 1.10x slower                                                 |
| crypto_pyaes            | 51.7 ms                                                | 57.1 ms: 1.10x slower                                                 |
| scimark_monte_carlo     | 46.4 ms                                                | 51.3 ms: 1.10x slower                                                 |
| dask                    | 226 ms                                                 | 255 ms: 1.13x slower                                                  |
| comprehensions          | 16.1 us                                                | 18.2 us: 1.13x slower                                                 |
| sqlglot_transpile       | 1.12 ms                                                | 1.36 ms: 1.22x slower                                                 |
| sqlglot_parse           | 957 us                                                 | 1.19 ms: 1.24x slower                                                 |
| python_startup          | 11.5 ms                                                | 15.6 ms: 1.35x slower                                                 |
| unpack_sequence         | 33.6 ns                                                | 90.8 ns: 2.71x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (8): nqueens, aiohttp, float, unpickle_list, asyncio_tcp, gunicorn, tornado_http, async_tree_memoization
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: mypy2
