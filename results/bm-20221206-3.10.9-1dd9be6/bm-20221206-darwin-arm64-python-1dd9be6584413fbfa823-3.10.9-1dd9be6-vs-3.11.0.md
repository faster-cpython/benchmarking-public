
# Results vs. 3.11.0

- fork: python
- ref: 1dd9be6584413fbfa823
- machine: darwin-arm64
- commit hash: 1dd9be6
- commit date: 2022-12-06
- overall geometric mean: 1.20x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-darwin-arm64-python-1dd9be6584413fbfa823-3.10.9-1dd9be6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 223 ms: 1.38x slower                                                |
| chameleon      | 4.60 ms                                                | 5.83 ms: 1.27x slower                                               |
| docutils       | 1.47 sec                                               | 1.77 sec: 1.20x slower                                              |
| html5lib       | 34.7 ms                                                | 46.5 ms: 1.34x slower                                               |
| tornado_http   | 71.5 ms                                                | 93.5 ms: 1.31x slower                                               |
| Geometric mean | (ref)                                                  | 1.30x slower                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-darwin-arm64-python-1dd9be6584413fbfa823-3.10.9-1dd9be6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 281 ms                                                 | 284 ms: 1.01x slower                                                |
| float          | 53.0 ms                                                | 72.1 ms: 1.36x slower                                               |
| nbody          | 65.6 ms                                                | 92.6 ms: 1.41x slower                                               |
| Geometric mean | (ref)                                                  | 1.25x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-darwin-arm64-python-1dd9be6584413fbfa823-3.10.9-1dd9be6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.64 ms: 1.00x slower                                               |
| regex_v8       | 16.1 ms                                                | 18.3 ms: 1.14x slower                                               |
| regex_dna      | 152 ms                                                 | 180 ms: 1.19x slower                                                |
| regex_compile  | 76.7 ms                                                | 96.5 ms: 1.26x slower                                               |
| Geometric mean | (ref)                                                  | 1.14x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-darwin-arm64-python-1dd9be6584413fbfa823-3.10.9-1dd9be6 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 100 ms: 1.08x faster                                                |
| xml_etree_iterparse  | 70.1 ms                                                | 69.0 ms: 1.02x faster                                               |
| unpickle_list        | 2.65 us                                                | 2.66 us: 1.01x slower                                               |
| unpickle             | 9.67 us                                                | 9.87 us: 1.02x slower                                               |
| pickle_dict          | 18.0 us                                                | 18.8 us: 1.05x slower                                               |
| pickle_list          | 2.81 us                                                | 2.96 us: 1.05x slower                                               |
| json_loads           | 16.1 us                                                | 17.0 us: 1.06x slower                                               |
| pickle               | 7.15 us                                                | 7.56 us: 1.06x slower                                               |
| json_dumps           | 7.63 ms                                                | 8.25 ms: 1.08x slower                                               |
| xml_etree_generate   | 48.3 ms                                                | 54.3 ms: 1.13x slower                                               |
| unpickle_pure_python | 159 us                                                 | 203 us: 1.27x slower                                                |
| xml_etree_process    | 35.1 ms                                                | 44.9 ms: 1.28x slower                                               |
| pickle_pure_python   | 201 us                                                 | 284 us: 1.42x slower                                                |
| Geometric mean       | (ref)                                                  | 1.09x slower                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-darwin-arm64-python-1dd9be6584413fbfa823-3.10.9-1dd9be6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 6.95 ms: 1.46x faster                                               |
| python_startup         | 12.4 ms                                                | 9.57 ms: 1.30x faster                                               |
| Geometric mean         | (ref)                                                  | 1.38x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-darwin-arm64-python-1dd9be6584413fbfa823-3.10.9-1dd9be6 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 15.3 ms                                                | 18.2 ms: 1.19x slower                                               |
| mako            | 8.53 ms                                                | 10.7 ms: 1.25x slower                                               |
| genshi_xml      | 29.8 ms                                                | 37.3 ms: 1.25x slower                                               |
| django_template | 21.0 ms                                                | 27.3 ms: 1.30x slower                                               |
| Geometric mean  | (ref)                                                  | 1.25x slower                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-darwin-arm64-python-1dd9be6584413fbfa823-3.10.9-1dd9be6 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site  | 10.2 ms                                                | 6.95 ms: 1.46x faster                                               |
| coverage                | 58.4 ms                                                | 40.6 ms: 1.44x faster                                               |
| python_startup          | 12.4 ms                                                | 9.57 ms: 1.30x faster                                               |
| pathlib                 | 27.2 ms                                                | 22.0 ms: 1.24x faster                                               |
| xml_etree_parse         | 108 ms                                                 | 100 ms: 1.08x faster                                                |
| bench_mp_pool           | 43.9 ms                                                | 40.8 ms: 1.08x faster                                               |
| xml_etree_iterparse     | 70.1 ms                                                | 69.0 ms: 1.02x faster                                               |
| regex_effbot            | 2.63 ms                                                | 2.64 ms: 1.00x slower                                               |
| unpickle_list           | 2.65 us                                                | 2.66 us: 1.01x slower                                               |
| pidigits                | 281 ms                                                 | 284 ms: 1.01x slower                                                |
| unpickle                | 9.67 us                                                | 9.87 us: 1.02x slower                                               |
| pickle_dict             | 18.0 us                                                | 18.8 us: 1.05x slower                                               |
| pickle_list             | 2.81 us                                                | 2.96 us: 1.05x slower                                               |
| meteor_contest          | 73.5 ms                                                | 77.4 ms: 1.05x slower                                               |
| json_loads              | 16.1 us                                                | 17.0 us: 1.06x slower                                               |
| pickle                  | 7.15 us                                                | 7.56 us: 1.06x slower                                               |
| telco                   | 3.41 ms                                                | 3.64 ms: 1.07x slower                                               |
| flaskblogging           | 2.43 ms                                                | 2.60 ms: 1.07x slower                                               |
| mdp                     | 1.55 sec                                               | 1.66 sec: 1.08x slower                                              |
| json_dumps              | 7.63 ms                                                | 8.25 ms: 1.08x slower                                               |
| scimark_sparse_mat_mult | 3.19 ms                                                | 3.46 ms: 1.09x slower                                               |
| bench_thread_pool       | 474 us                                                 | 518 us: 1.09x slower                                                |
| unpack_sequence         | 34.1 ns                                                | 37.4 ns: 1.10x slower                                               |
| pylint                  | 272 ms                                                 | 300 ms: 1.11x slower                                                |
| sympy_sum               | 85.5 ms                                                | 95.4 ms: 1.12x slower                                               |
| json                    | 2.78 ms                                                | 3.11 ms: 1.12x slower                                               |
| sympy_str               | 151 ms                                                 | 170 ms: 1.12x slower                                                |
| xml_etree_generate      | 48.3 ms                                                | 54.3 ms: 1.13x slower                                               |
| generators              | 28.8 ms                                                | 32.4 ms: 1.13x slower                                               |
| aiohttp                 | 1.05 ms                                                | 1.19 ms: 1.13x slower                                               |
| gunicorn                | 1.11 ms                                                | 1.26 ms: 1.13x slower                                               |
| coroutines              | 17.8 ms                                                | 20.1 ms: 1.13x slower                                               |
| regex_v8                | 16.1 ms                                                | 18.3 ms: 1.14x slower                                               |
| nqueens                 | 59.8 ms                                                | 68.1 ms: 1.14x slower                                               |
| sympy_expand            | 242 ms                                                 | 276 ms: 1.14x slower                                                |
| sqlglot_normalize       | 171 ms                                                 | 196 ms: 1.15x slower                                                |
| scimark_fft             | 200 ms                                                 | 230 ms: 1.15x slower                                                |
| sympy_integrate         | 11.5 ms                                                | 13.4 ms: 1.16x slower                                               |
| sqlite_synth            | 1.27 us                                                | 1.49 us: 1.17x slower                                               |
| async_generators        | 196 ms                                                 | 231 ms: 1.18x slower                                                |
| regex_dna               | 152 ms                                                 | 180 ms: 1.19x slower                                                |
| genshi_text             | 15.3 ms                                                | 18.2 ms: 1.19x slower                                               |
| sqlalchemy_declarative  | 62.6 ms                                                | 74.5 ms: 1.19x slower                                               |
| docutils                | 1.47 sec                                               | 1.77 sec: 1.20x slower                                              |
| dulwich_log             | 30.3 ms                                                | 36.7 ms: 1.21x slower                                               |
| fannkuch                | 261 ms                                                 | 318 ms: 1.22x slower                                                |
| sqlglot_optimize        | 31.1 ms                                                | 37.9 ms: 1.22x slower                                               |
| deepcopy_reduce         | 1.91 us                                                | 2.34 us: 1.22x slower                                               |
| async_tree_cpu_io_mixed | 533 ms                                                 | 661 ms: 1.24x slower                                                |
| sqlalchemy_imperative   | 7.20 ms                                                | 8.96 ms: 1.24x slower                                               |
| mako                    | 8.53 ms                                                | 10.7 ms: 1.25x slower                                               |
| genshi_xml              | 29.8 ms                                                | 37.3 ms: 1.25x slower                                               |
| deepcopy                | 223 us                                                 | 280 us: 1.26x slower                                                |
| regex_compile           | 76.7 ms                                                | 96.5 ms: 1.26x slower                                               |
| chameleon               | 4.60 ms                                                | 5.83 ms: 1.27x slower                                               |
| unpickle_pure_python    | 159 us                                                 | 203 us: 1.27x slower                                                |
| xml_etree_process       | 35.1 ms                                                | 44.9 ms: 1.28x slower                                               |
| pprint_pformat          | 954 ms                                                 | 1.23 sec: 1.29x slower                                              |
| pprint_safe_repr        | 466 ms                                                 | 603 ms: 1.29x slower                                                |
| django_template         | 21.0 ms                                                | 27.3 ms: 1.30x slower                                               |
| logging_simple          | 3.55 us                                                | 4.63 us: 1.31x slower                                               |
| tornado_http            | 71.5 ms                                                | 93.5 ms: 1.31x slower                                               |
| pycparser               | 698 ms                                                 | 912 ms: 1.31x slower                                                |
| deepcopy_memo           | 26.3 us                                                | 34.5 us: 1.31x slower                                               |
| thrift                  | 442 us                                                 | 582 us: 1.32x slower                                                |
| logging_format          | 3.78 us                                                | 4.99 us: 1.32x slower                                               |
| spectral_norm           | 72.6 ms                                                | 96.2 ms: 1.33x slower                                               |
| hexiom                  | 4.72 ms                                                | 6.30 ms: 1.34x slower                                               |
| html5lib                | 34.7 ms                                                | 46.5 ms: 1.34x slower                                               |
| chaos                   | 49.4 ms                                                | 66.6 ms: 1.35x slower                                               |
| float                   | 53.0 ms                                                | 72.1 ms: 1.36x slower                                               |
| sqlglot_transpile       | 1.12 ms                                                | 1.55 ms: 1.38x slower                                               |
| async_tree_none         | 286 ms                                                 | 394 ms: 1.38x slower                                                |
| 2to3                    | 161 ms                                                 | 223 ms: 1.38x slower                                                |
| sqlglot_parse           | 959 us                                                 | 1.33 ms: 1.39x slower                                               |
| nbody                   | 65.6 ms                                                | 92.6 ms: 1.41x slower                                               |
| pickle_pure_python      | 201 us                                                 | 284 us: 1.42x slower                                                |
| async_tree_io           | 704 ms                                                 | 1.00 sec: 1.42x slower                                              |
| async_tree_memoization  | 336 ms                                                 | 481 ms: 1.43x slower                                                |
| pyflate                 | 310 ms                                                 | 453 ms: 1.46x slower                                                |
| scimark_lu              | 73.3 ms                                                | 110 ms: 1.49x slower                                                |
| crypto_pyaes            | 51.7 ms                                                | 77.9 ms: 1.51x slower                                               |
| go                      | 109 ms                                                 | 165 ms: 1.52x slower                                                |
| scimark_sor             | 82.6 ms                                                | 126 ms: 1.53x slower                                                |
| scimark_monte_carlo     | 46.5 ms                                                | 72.0 ms: 1.55x slower                                               |
| raytrace                | 207 ms                                                 | 327 ms: 1.58x slower                                                |
| richards                | 32.2 ms                                                | 51.0 ms: 1.58x slower                                               |
| logging_silent          | 68.1 ns                                                | 118 ns: 1.74x slower                                                |
| deltablue               | 2.81 ms                                                | 5.15 ms: 1.83x slower                                               |
| Geometric mean          | (ref)                                                  | 1.20x slower                                                        |
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, gc_traversal, mypy2, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221206-3.10.9-1dd9be6/bm-20221206-darwin-arm64-python-1dd9be6584413fbfa823-3.10.9-1dd9be6.json: mypy


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.19x
- 95% likely to have a slowdown of 1.18x
- 99% likely to have a slowdown of 1.16x
