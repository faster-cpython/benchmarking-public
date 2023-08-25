
# Results vs. 3.11.0

- fork: python
- ref: e2b4e4bab90b69fbd361
- machine: darwin-arm64
- commit hash: e2b4e4b
- commit date: 2021-11-05
- overall geometric mean: 1.05x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 166 ms: 1.03x slower                                                  |
| chameleon      | 4.60 ms                                                | 5.09 ms: 1.11x slower                                                 |
| docutils       | 1.47 sec                                               | 1.54 sec: 1.05x slower                                                |
| html5lib       | 34.7 ms                                                | 36.7 ms: 1.06x slower                                                 |
| tornado_http   | 71.5 ms                                                | 76.5 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 53.0 ms                                                | 52.0 ms: 1.02x faster                                                 |
| nbody          | 65.6 ms                                                | 74.3 ms: 1.13x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.45 ms: 1.07x faster                                                 |
| regex_compile  | 76.7 ms                                                | 78.0 ms: 1.02x slower                                                 |
| regex_dna      | 152 ms                                                 | 162 ms: 1.07x slower                                                  |
| regex_v8       | 16.1 ms                                                | 17.5 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 101 ms: 1.07x faster                                                  |
| unpickle_list        | 2.65 us                                                | 2.52 us: 1.05x faster                                                 |
| pickle_dict          | 18.0 us                                                | 17.6 us: 1.02x faster                                                 |
| xml_etree_generate   | 48.3 ms                                                | 48.8 ms: 1.01x slower                                                 |
| pickle               | 7.15 us                                                | 7.26 us: 1.02x slower                                                 |
| json_dumps           | 7.63 ms                                                | 7.85 ms: 1.03x slower                                                 |
| json_loads           | 16.1 us                                                | 16.6 us: 1.03x slower                                                 |
| unpickle             | 9.67 us                                                | 10.1 us: 1.04x slower                                                 |
| xml_etree_process    | 35.1 ms                                                | 36.9 ms: 1.05x slower                                                 |
| unpickle_pure_python | 159 us                                                 | 176 us: 1.10x slower                                                  |
| pickle_pure_python   | 201 us                                                 | 229 us: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 9.29 ms: 1.09x faster                                                 |
| python_startup         | 12.4 ms                                                | 15.9 ms: 1.28x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 15.3 ms                                                | 15.7 ms: 1.03x slower                                                 |
| genshi_xml      | 29.8 ms                                                | 30.9 ms: 1.04x slower                                                 |
| django_template | 21.0 ms                                                | 22.7 ms: 1.08x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coverage                | 58.4 ms                                                | 43.4 ms: 1.35x faster                                                 |
| python_startup_no_site  | 10.2 ms                                                | 9.29 ms: 1.09x faster                                                 |
| unpack_sequence         | 34.1 ns                                                | 31.3 ns: 1.09x faster                                                 |
| regex_effbot            | 2.63 ms                                                | 2.45 ms: 1.07x faster                                                 |
| xml_etree_parse         | 108 ms                                                 | 101 ms: 1.07x faster                                                  |
| unpickle_list           | 2.65 us                                                | 2.52 us: 1.05x faster                                                 |
| bench_mp_pool           | 43.9 ms                                                | 42.0 ms: 1.05x faster                                                 |
| pathlib                 | 27.2 ms                                                | 26.5 ms: 1.03x faster                                                 |
| logging_simple          | 3.55 us                                                | 3.47 us: 1.02x faster                                                 |
| pickle_dict             | 18.0 us                                                | 17.6 us: 1.02x faster                                                 |
| float                   | 53.0 ms                                                | 52.0 ms: 1.02x faster                                                 |
| logging_format          | 3.78 us                                                | 3.73 us: 1.01x faster                                                 |
| generators              | 28.8 ms                                                | 28.5 ms: 1.01x faster                                                 |
| chaos                   | 49.4 ms                                                | 49.2 ms: 1.00x faster                                                 |
| telco                   | 3.41 ms                                                | 3.39 ms: 1.00x faster                                                 |
| gc_traversal            | 2.42 ms                                                | 2.43 ms: 1.00x slower                                                 |
| scimark_fft             | 200 ms                                                 | 201 ms: 1.01x slower                                                  |
| async_generators        | 196 ms                                                 | 198 ms: 1.01x slower                                                  |
| raytrace                | 207 ms                                                 | 209 ms: 1.01x slower                                                  |
| sympy_sum               | 85.5 ms                                                | 86.3 ms: 1.01x slower                                                 |
| meteor_contest          | 73.5 ms                                                | 74.2 ms: 1.01x slower                                                 |
| xml_etree_generate      | 48.3 ms                                                | 48.8 ms: 1.01x slower                                                 |
| pickle                  | 7.15 us                                                | 7.26 us: 1.02x slower                                                 |
| regex_compile           | 76.7 ms                                                | 78.0 ms: 1.02x slower                                                 |
| mdp                     | 1.55 sec                                               | 1.57 sec: 1.02x slower                                                |
| scimark_sparse_mat_mult | 3.19 ms                                                | 3.25 ms: 1.02x slower                                                 |
| sqlglot_normalize       | 171 ms                                                 | 175 ms: 1.02x slower                                                  |
| flaskblogging           | 2.43 ms                                                | 2.49 ms: 1.02x slower                                                 |
| genshi_text             | 15.3 ms                                                | 15.7 ms: 1.03x slower                                                 |
| create_gc_cycles        | 716 us                                                 | 735 us: 1.03x slower                                                  |
| async_tree_none         | 286 ms                                                 | 294 ms: 1.03x slower                                                  |
| json_dumps              | 7.63 ms                                                | 7.85 ms: 1.03x slower                                                 |
| nqueens                 | 59.8 ms                                                | 61.6 ms: 1.03x slower                                                 |
| gunicorn                | 1.11 ms                                                | 1.15 ms: 1.03x slower                                                 |
| json_loads              | 16.1 us                                                | 16.6 us: 1.03x slower                                                 |
| 2to3                    | 161 ms                                                 | 166 ms: 1.03x slower                                                  |
| dulwich_log             | 30.3 ms                                                | 31.3 ms: 1.03x slower                                                 |
| spectral_norm           | 72.6 ms                                                | 75.1 ms: 1.03x slower                                                 |
| genshi_xml              | 29.8 ms                                                | 30.9 ms: 1.04x slower                                                 |
| unpickle                | 9.67 us                                                | 10.1 us: 1.04x slower                                                 |
| pylint                  | 272 ms                                                 | 283 ms: 1.04x slower                                                  |
| sqlalchemy_declarative  | 62.6 ms                                                | 65.3 ms: 1.04x slower                                                 |
| hexiom                  | 4.72 ms                                                | 4.93 ms: 1.04x slower                                                 |
| docutils                | 1.47 sec                                               | 1.54 sec: 1.05x slower                                                |
| sympy_str               | 151 ms                                                 | 158 ms: 1.05x slower                                                  |
| xml_etree_process       | 35.1 ms                                                | 36.9 ms: 1.05x slower                                                 |
| sympy_integrate         | 11.5 ms                                                | 12.1 ms: 1.05x slower                                                 |
| sympy_expand            | 242 ms                                                 | 256 ms: 1.06x slower                                                  |
| html5lib                | 34.7 ms                                                | 36.7 ms: 1.06x slower                                                 |
| deepcopy_memo           | 26.3 us                                                | 27.8 us: 1.06x slower                                                 |
| thrift                  | 442 us                                                 | 467 us: 1.06x slower                                                  |
| scimark_monte_carlo     | 46.5 ms                                                | 49.2 ms: 1.06x slower                                                 |
| regex_dna               | 152 ms                                                 | 162 ms: 1.07x slower                                                  |
| sqlalchemy_imperative   | 7.20 ms                                                | 7.69 ms: 1.07x slower                                                 |
| pprint_safe_repr        | 466 ms                                                 | 499 ms: 1.07x slower                                                  |
| fannkuch                | 261 ms                                                 | 279 ms: 1.07x slower                                                  |
| tornado_http            | 71.5 ms                                                | 76.5 ms: 1.07x slower                                                 |
| pprint_pformat          | 954 ms                                                 | 1.02 sec: 1.07x slower                                                |
| deepcopy                | 223 us                                                 | 239 us: 1.07x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                | 2.05 us: 1.07x slower                                                 |
| json                    | 2.78 ms                                                | 2.98 ms: 1.07x slower                                                 |
| django_template         | 21.0 ms                                                | 22.7 ms: 1.08x slower                                                 |
| sqlglot_optimize        | 31.1 ms                                                | 33.6 ms: 1.08x slower                                                 |
| sqlite_synth            | 1.27 us                                                | 1.38 us: 1.08x slower                                                 |
| coroutines              | 17.8 ms                                                | 19.3 ms: 1.09x slower                                                 |
| bench_thread_pool       | 474 us                                                 | 516 us: 1.09x slower                                                  |
| comprehensions          | 16.1 us                                                | 17.5 us: 1.09x slower                                                 |
| regex_v8                | 16.1 ms                                                | 17.5 ms: 1.09x slower                                                 |
| async_tree_memoization  | 336 ms                                                 | 367 ms: 1.09x slower                                                  |
| go                      | 109 ms                                                 | 119 ms: 1.10x slower                                                  |
| pycparser               | 698 ms                                                 | 767 ms: 1.10x slower                                                  |
| async_tree_cpu_io_mixed | 533 ms                                                 | 587 ms: 1.10x slower                                                  |
| unpickle_pure_python    | 159 us                                                 | 176 us: 1.10x slower                                                  |
| chameleon               | 4.60 ms                                                | 5.09 ms: 1.11x slower                                                 |
| crypto_pyaes            | 51.7 ms                                                | 58.2 ms: 1.13x slower                                                 |
| async_tree_io           | 704 ms                                                 | 794 ms: 1.13x slower                                                  |
| nbody                   | 65.6 ms                                                | 74.3 ms: 1.13x slower                                                 |
| pickle_pure_python      | 201 us                                                 | 229 us: 1.14x slower                                                  |
| deltablue               | 2.81 ms                                                | 3.23 ms: 1.15x slower                                                 |
| pyflate                 | 310 ms                                                 | 360 ms: 1.16x slower                                                  |
| richards                | 32.2 ms                                                | 37.7 ms: 1.17x slower                                                 |
| scimark_sor             | 82.6 ms                                                | 99.5 ms: 1.20x slower                                                 |
| logging_silent          | 68.1 ns                                                | 82.2 ns: 1.21x slower                                                 |
| sqlglot_transpile       | 1.12 ms                                                | 1.41 ms: 1.26x slower                                                 |
| python_startup          | 12.4 ms                                                | 15.9 ms: 1.28x slower                                                 |
| scimark_lu              | 73.3 ms                                                | 93.8 ms: 1.28x slower                                                 |
| sqlglot_parse           | 959 us                                                 | 1.24 ms: 1.29x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.05x slower                                                          |

Benchmark hidden because not significant (4): xml_etree_iterparse, pidigits, pickle_list, mako
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, mypy2, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20211105-3.11.0a2-e2b4e4b/bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b.json: dask


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x
