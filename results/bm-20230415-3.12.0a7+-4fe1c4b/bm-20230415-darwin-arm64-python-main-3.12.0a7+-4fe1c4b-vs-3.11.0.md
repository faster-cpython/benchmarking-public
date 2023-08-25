
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 4fe1c4b
- commit date: 2023-04-15
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-darwin-arm64-python-main-3.12.0a7+-4fe1c4b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 161 ms: 1.01x faster                                   |
| chameleon      | 4.60 ms                                                | 4.23 ms: 1.09x faster                                  |
| docutils       | 1.47 sec                                               | 1.45 sec: 1.01x faster                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-darwin-arm64-python-main-3.12.0a7+-4fe1c4b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 56.7 ms: 1.16x faster                                  |
| float          | 53.0 ms                                                | 50.9 ms: 1.04x faster                                  |
| pidigits       | 281 ms                                                 | 280 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-darwin-arm64-python-main-3.12.0a7+-4fe1c4b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 72.3 ms: 1.06x faster                                  |
| regex_v8       | 16.1 ms                                                | 15.7 ms: 1.03x faster                                  |
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                   |
| regex_effbot   | 2.63 ms                                                | 2.61 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-darwin-arm64-python-main-3.12.0a7+-4fe1c4b |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.04 ms: 1.26x faster                                  |
| unpickle_pure_python | 159 us                                                 | 137 us: 1.16x faster                                   |
| xml_etree_parse      | 108 ms                                                 | 97.5 ms: 1.11x faster                                  |
| pickle_pure_python   | 201 us                                                 | 182 us: 1.10x faster                                   |
| unpickle             | 9.67 us                                                | 8.99 us: 1.08x faster                                  |
| xml_etree_iterparse  | 70.1 ms                                                | 68.4 ms: 1.03x faster                                  |
| xml_etree_process    | 35.1 ms                                                | 34.5 ms: 1.02x faster                                  |
| unpickle_list        | 2.65 us                                                | 2.62 us: 1.01x faster                                  |
| json_loads           | 16.1 us                                                | 16.3 us: 1.01x slower                                  |
| xml_etree_generate   | 48.3 ms                                                | 49.0 ms: 1.02x slower                                  |
| pickle_dict          | 18.0 us                                                | 18.5 us: 1.03x slower                                  |
| pickle_list          | 2.81 us                                                | 2.91 us: 1.03x slower                                  |
| pickle               | 7.15 us                                                | 7.50 us: 1.05x slower                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-darwin-arm64-python-main-3.12.0a7+-4fe1c4b |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.4 ms                                                | 11.5 ms: 1.08x faster                                  |
| python_startup_no_site | 10.2 ms                                                | 9.51 ms: 1.07x faster                                  |
| Geometric mean         | (ref)                                                  | 1.07x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-darwin-arm64-python-main-3.12.0a7+-4fe1c4b |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 8.53 ms                                                | 7.04 ms: 1.21x faster                                  |
| genshi_text     | 15.3 ms                                                | 13.4 ms: 1.14x faster                                  |
| genshi_xml      | 29.8 ms                                                | 26.4 ms: 1.13x faster                                  |
| django_template | 21.0 ms                                                | 20.2 ms: 1.04x faster                                  |
| Geometric mean  | (ref)                                                  | 1.13x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-darwin-arm64-python-main-3.12.0a7+-4fe1c4b |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 429 ms: 1.52x faster                                   |
| generators              | 28.8 ms                                                | 22.5 ms: 1.28x faster                                  |
| json_dumps              | 7.63 ms                                                | 6.04 ms: 1.26x faster                                  |
| mako                    | 8.53 ms                                                | 7.04 ms: 1.21x faster                                  |
| scimark_sparse_mat_mult | 3.19 ms                                                | 2.71 ms: 1.18x faster                                  |
| unpickle_pure_python    | 159 us                                                 | 137 us: 1.16x faster                                   |
| nbody                   | 65.6 ms                                                | 56.7 ms: 1.16x faster                                  |
| unpack_sequence         | 34.1 ns                                                | 29.5 ns: 1.16x faster                                  |
| sqlglot_parse           | 959 us                                                 | 831 us: 1.15x faster                                   |
| hexiom                  | 4.72 ms                                                | 4.10 ms: 1.15x faster                                  |
| genshi_text             | 15.3 ms                                                | 13.4 ms: 1.14x faster                                  |
| sqlglot_transpile       | 1.12 ms                                                | 992 us: 1.13x faster                                   |
| genshi_xml              | 29.8 ms                                                | 26.4 ms: 1.13x faster                                  |
| deltablue               | 2.81 ms                                                | 2.50 ms: 1.13x faster                                  |
| coverage                | 58.4 ms                                                | 52.1 ms: 1.12x faster                                  |
| scimark_fft             | 200 ms                                                 | 179 ms: 1.11x faster                                   |
| xml_etree_parse         | 108 ms                                                 | 97.5 ms: 1.11x faster                                  |
| pickle_pure_python      | 201 us                                                 | 182 us: 1.10x faster                                   |
| logging_silent          | 68.1 ns                                                | 62.1 ns: 1.10x faster                                  |
| chaos                   | 49.4 ms                                                | 45.2 ms: 1.09x faster                                  |
| scimark_lu              | 73.3 ms                                                | 67.3 ms: 1.09x faster                                  |
| chameleon               | 4.60 ms                                                | 4.23 ms: 1.09x faster                                  |
| deepcopy_memo           | 26.3 us                                                | 24.3 us: 1.08x faster                                  |
| python_startup          | 12.4 ms                                                | 11.5 ms: 1.08x faster                                  |
| unpickle                | 9.67 us                                                | 8.99 us: 1.08x faster                                  |
| spectral_norm           | 72.6 ms                                                | 67.8 ms: 1.07x faster                                  |
| python_startup_no_site  | 10.2 ms                                                | 9.51 ms: 1.07x faster                                  |
| regex_compile           | 76.7 ms                                                | 72.3 ms: 1.06x faster                                  |
| pylint                  | 272 ms                                                 | 256 ms: 1.06x faster                                   |
| pycparser               | 698 ms                                                 | 658 ms: 1.06x faster                                   |
| pprint_safe_repr        | 466 ms                                                 | 440 ms: 1.06x faster                                   |
| pprint_pformat          | 954 ms                                                 | 902 ms: 1.06x faster                                   |
| deepcopy                | 223 us                                                 | 211 us: 1.05x faster                                   |
| richards                | 32.2 ms                                                | 30.7 ms: 1.05x faster                                  |
| async_tree_memoization  | 336 ms                                                 | 320 ms: 1.05x faster                                   |
| deepcopy_reduce         | 1.91 us                                                | 1.83 us: 1.04x faster                                  |
| sqlglot_normalize       | 171 ms                                                 | 164 ms: 1.04x faster                                   |
| bench_thread_pool       | 474 us                                                 | 455 us: 1.04x faster                                   |
| sqlglot_optimize        | 31.1 ms                                                | 29.9 ms: 1.04x faster                                  |
| float                   | 53.0 ms                                                | 50.9 ms: 1.04x faster                                  |
| django_template         | 21.0 ms                                                | 20.2 ms: 1.04x faster                                  |
| dulwich_log             | 30.3 ms                                                | 29.2 ms: 1.04x faster                                  |
| coroutines              | 17.8 ms                                                | 17.2 ms: 1.03x faster                                  |
| meteor_contest          | 73.5 ms                                                | 71.3 ms: 1.03x faster                                  |
| async_tree_none         | 286 ms                                                 | 277 ms: 1.03x faster                                   |
| mdp                     | 1.55 sec                                               | 1.50 sec: 1.03x faster                                 |
| regex_v8                | 16.1 ms                                                | 15.7 ms: 1.03x faster                                  |
| sympy_integrate         | 11.5 ms                                                | 11.2 ms: 1.03x faster                                  |
| xml_etree_iterparse     | 70.1 ms                                                | 68.4 ms: 1.03x faster                                  |
| logging_simple          | 3.55 us                                                | 3.46 us: 1.02x faster                                  |
| create_gc_cycles        | 716 us                                                 | 700 us: 1.02x faster                                   |
| comprehensions          | 16.1 us                                                | 15.8 us: 1.02x faster                                  |
| sympy_expand            | 242 ms                                                 | 237 ms: 1.02x faster                                   |
| sympy_str               | 151 ms                                                 | 148 ms: 1.02x faster                                   |
| regex_dna               | 152 ms                                                 | 149 ms: 1.02x faster                                   |
| sqlalchemy_imperative   | 7.20 ms                                                | 7.07 ms: 1.02x faster                                  |
| xml_etree_process       | 35.1 ms                                                | 34.5 ms: 1.02x faster                                  |
| sqlalchemy_declarative  | 62.6 ms                                                | 61.6 ms: 1.02x faster                                  |
| fannkuch                | 261 ms                                                 | 257 ms: 1.01x faster                                   |
| telco                   | 3.41 ms                                                | 3.36 ms: 1.01x faster                                  |
| docutils                | 1.47 sec                                               | 1.45 sec: 1.01x faster                                 |
| unpickle_list           | 2.65 us                                                | 2.62 us: 1.01x faster                                  |
| scimark_sor             | 82.6 ms                                                | 81.8 ms: 1.01x faster                                  |
| regex_effbot            | 2.63 ms                                                | 2.61 ms: 1.01x faster                                  |
| sympy_sum               | 85.5 ms                                                | 84.9 ms: 1.01x faster                                  |
| 2to3                    | 161 ms                                                 | 161 ms: 1.01x faster                                   |
| thrift                  | 442 us                                                 | 440 us: 1.00x faster                                   |
| pidigits                | 281 ms                                                 | 280 ms: 1.00x faster                                   |
| gc_traversal            | 2.42 ms                                                | 2.43 ms: 1.01x slower                                  |
| json_loads              | 16.1 us                                                | 16.3 us: 1.01x slower                                  |
| go                      | 109 ms                                                 | 110 ms: 1.01x slower                                   |
| xml_etree_generate      | 48.3 ms                                                | 49.0 ms: 1.02x slower                                  |
| async_tree_io           | 704 ms                                                 | 716 ms: 1.02x slower                                   |
| raytrace                | 207 ms                                                 | 212 ms: 1.02x slower                                   |
| bench_mp_pool           | 43.9 ms                                                | 45.1 ms: 1.03x slower                                  |
| pickle_dict             | 18.0 us                                                | 18.5 us: 1.03x slower                                  |
| crypto_pyaes            | 51.7 ms                                                | 53.4 ms: 1.03x slower                                  |
| pickle_list             | 2.81 us                                                | 2.91 us: 1.03x slower                                  |
| pickle                  | 7.15 us                                                | 7.50 us: 1.05x slower                                  |
| scimark_monte_carlo     | 46.5 ms                                                | 48.9 ms: 1.05x slower                                  |
| pyflate                 | 310 ms                                                 | 327 ms: 1.05x slower                                   |
| sqlite_synth            | 1.27 us                                                | 1.35 us: 1.06x slower                                  |
| async_generators        | 196 ms                                                 | 257 ms: 1.31x slower                                   |
| mypy2                   | 195 ms                                                 | 256 ms: 1.31x slower                                   |
| Geometric mean          | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (7): tornado_http, pathlib, async_tree_cpu_io_mixed, logging_format, json, nqueens, html5lib
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230415-3.12.0a7+-4fe1c4b/bm-20230415-darwin-arm64-python-main-3.12.0a7+-4fe1c4b.json: dask


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
