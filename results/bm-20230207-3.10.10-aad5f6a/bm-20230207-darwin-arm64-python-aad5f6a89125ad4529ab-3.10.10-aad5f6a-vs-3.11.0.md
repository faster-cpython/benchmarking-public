
# Results vs. 3.11.0

- fork: python
- ref: aad5f6a89125ad4529ab
- machine: darwin-arm64
- commit hash: aad5f6a
- commit date: 2023-02-07
- overall geometric mean: 1.22x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-darwin-arm64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 203 ms: 1.26x slower                                                 |
| chameleon      | 4.60 ms                                                | 5.78 ms: 1.26x slower                                                |
| docutils       | 1.47 sec                                               | 1.79 sec: 1.22x slower                                               |
| html5lib       | 34.7 ms                                                | 47.8 ms: 1.38x slower                                                |
| tornado_http   | 71.5 ms                                                | 92.9 ms: 1.30x slower                                                |
| Geometric mean | (ref)                                                  | 1.28x slower                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-darwin-arm64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                                 |
| float          | 53.0 ms                                                | 72.3 ms: 1.37x slower                                                |
| nbody          | 65.6 ms                                                | 94.1 ms: 1.43x slower                                                |
| Geometric mean | (ref)                                                  | 1.25x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-darwin-arm64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.75 ms: 1.05x slower                                                |
| regex_v8       | 16.1 ms                                                | 18.2 ms: 1.13x slower                                                |
| regex_dna      | 152 ms                                                 | 187 ms: 1.23x slower                                                 |
| regex_compile  | 76.7 ms                                                | 96.9 ms: 1.26x slower                                                |
| Geometric mean | (ref)                                                  | 1.16x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-darwin-arm64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 107 ms: 1.01x faster                                                 |
| unpickle_list        | 2.65 us                                                | 2.68 us: 1.01x slower                                                |
| unpickle             | 9.67 us                                                | 9.86 us: 1.02x slower                                                |
| pickle_list          | 2.81 us                                                | 2.93 us: 1.04x slower                                                |
| pickle_dict          | 18.0 us                                                | 18.7 us: 1.04x slower                                                |
| xml_etree_iterparse  | 70.1 ms                                                | 73.1 ms: 1.04x slower                                                |
| json_loads           | 16.1 us                                                | 16.9 us: 1.05x slower                                                |
| pickle               | 7.15 us                                                | 7.54 us: 1.05x slower                                                |
| json_dumps           | 7.63 ms                                                | 8.29 ms: 1.09x slower                                                |
| xml_etree_generate   | 48.3 ms                                                | 55.0 ms: 1.14x slower                                                |
| unpickle_pure_python | 159 us                                                 | 204 us: 1.28x slower                                                 |
| xml_etree_process    | 35.1 ms                                                | 45.0 ms: 1.28x slower                                                |
| pickle_pure_python   | 201 us                                                 | 287 us: 1.43x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.11x slower                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-darwin-arm64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 9.82 ms: 1.04x faster                                                |
| python_startup         | 12.4 ms                                                | 12.7 ms: 1.02x slower                                                |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-darwin-arm64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 15.3 ms                                                | 18.2 ms: 1.19x slower                                                |
| mako            | 8.53 ms                                                | 10.5 ms: 1.23x slower                                                |
| genshi_xml      | 29.8 ms                                                | 37.3 ms: 1.25x slower                                                |
| django_template | 21.0 ms                                                | 27.2 ms: 1.29x slower                                                |
| Geometric mean  | (ref)                                                  | 1.24x slower                                                         |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-darwin-arm64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| coverage                | 58.4 ms                                                | 41.8 ms: 1.40x faster                                                |
| bench_mp_pool           | 43.9 ms                                                | 40.9 ms: 1.07x faster                                                |
| python_startup_no_site  | 10.2 ms                                                | 9.82 ms: 1.04x faster                                                |
| xml_etree_parse         | 108 ms                                                 | 107 ms: 1.01x faster                                                 |
| gc_traversal            | 2.42 ms                                                | 2.40 ms: 1.01x faster                                                |
| pidigits                | 281 ms                                                 | 282 ms: 1.00x slower                                                 |
| unpickle_list           | 2.65 us                                                | 2.68 us: 1.01x slower                                                |
| unpickle                | 9.67 us                                                | 9.86 us: 1.02x slower                                                |
| python_startup          | 12.4 ms                                                | 12.7 ms: 1.02x slower                                                |
| asyncio_tcp             | 651 ms                                                 | 673 ms: 1.03x slower                                                 |
| pickle_list             | 2.81 us                                                | 2.93 us: 1.04x slower                                                |
| pickle_dict             | 18.0 us                                                | 18.7 us: 1.04x slower                                                |
| xml_etree_iterparse     | 70.1 ms                                                | 73.1 ms: 1.04x slower                                                |
| regex_effbot            | 2.63 ms                                                | 2.75 ms: 1.05x slower                                                |
| json_loads              | 16.1 us                                                | 16.9 us: 1.05x slower                                                |
| pathlib                 | 27.2 ms                                                | 28.7 ms: 1.05x slower                                                |
| pickle                  | 7.15 us                                                | 7.54 us: 1.05x slower                                                |
| meteor_contest          | 73.5 ms                                                | 77.6 ms: 1.06x slower                                                |
| telco                   | 3.41 ms                                                | 3.65 ms: 1.07x slower                                                |
| mdp                     | 1.55 sec                                               | 1.67 sec: 1.08x slower                                               |
| json_dumps              | 7.63 ms                                                | 8.29 ms: 1.09x slower                                                |
| scimark_sparse_mat_mult | 3.19 ms                                                | 3.48 ms: 1.09x slower                                                |
| comprehensions          | 16.1 us                                                | 17.7 us: 1.10x slower                                                |
| json                    | 2.78 ms                                                | 3.08 ms: 1.11x slower                                                |
| unpack_sequence         | 34.1 ns                                                | 38.3 ns: 1.12x slower                                                |
| bench_thread_pool       | 474 us                                                 | 534 us: 1.13x slower                                                 |
| pylint                  | 272 ms                                                 | 307 ms: 1.13x slower                                                 |
| regex_v8                | 16.1 ms                                                | 18.2 ms: 1.13x slower                                                |
| flaskblogging           | 2.43 ms                                                | 2.74 ms: 1.13x slower                                                |
| sympy_str               | 151 ms                                                 | 171 ms: 1.13x slower                                                 |
| sympy_sum               | 85.5 ms                                                | 96.8 ms: 1.13x slower                                                |
| coroutines              | 17.8 ms                                                | 20.2 ms: 1.13x slower                                                |
| generators              | 28.8 ms                                                | 32.7 ms: 1.14x slower                                                |
| nqueens                 | 59.8 ms                                                | 68.1 ms: 1.14x slower                                                |
| xml_etree_generate      | 48.3 ms                                                | 55.0 ms: 1.14x slower                                                |
| sqlglot_normalize       | 171 ms                                                 | 196 ms: 1.15x slower                                                 |
| sympy_expand            | 242 ms                                                 | 278 ms: 1.15x slower                                                 |
| sqlite_synth            | 1.27 us                                                | 1.47 us: 1.15x slower                                                |
| scimark_fft             | 200 ms                                                 | 232 ms: 1.16x slower                                                 |
| sympy_integrate         | 11.5 ms                                                | 13.4 ms: 1.17x slower                                                |
| genshi_text             | 15.3 ms                                                | 18.2 ms: 1.19x slower                                                |
| async_generators        | 196 ms                                                 | 234 ms: 1.19x slower                                                 |
| sqlalchemy_declarative  | 62.6 ms                                                | 74.8 ms: 1.20x slower                                                |
| aiohttp                 | 1.05 ms                                                | 1.26 ms: 1.20x slower                                                |
| gunicorn                | 1.11 ms                                                | 1.34 ms: 1.20x slower                                                |
| fannkuch                | 261 ms                                                 | 317 ms: 1.21x slower                                                 |
| docutils                | 1.47 sec                                               | 1.79 sec: 1.22x slower                                               |
| sqlglot_optimize        | 31.1 ms                                                | 38.0 ms: 1.22x slower                                                |
| create_gc_cycles        | 716 us                                                 | 878 us: 1.23x slower                                                 |
| dulwich_log             | 30.3 ms                                                | 37.2 ms: 1.23x slower                                                |
| regex_dna               | 152 ms                                                 | 187 ms: 1.23x slower                                                 |
| deepcopy_reduce         | 1.91 us                                                | 2.35 us: 1.23x slower                                                |
| mako                    | 8.53 ms                                                | 10.5 ms: 1.23x slower                                                |
| async_tree_cpu_io_mixed | 533 ms                                                 | 667 ms: 1.25x slower                                                 |
| genshi_xml              | 29.8 ms                                                | 37.3 ms: 1.25x slower                                                |
| chameleon               | 4.60 ms                                                | 5.78 ms: 1.26x slower                                                |
| 2to3                    | 161 ms                                                 | 203 ms: 1.26x slower                                                 |
| deepcopy                | 223 us                                                 | 280 us: 1.26x slower                                                 |
| regex_compile           | 76.7 ms                                                | 96.9 ms: 1.26x slower                                                |
| sqlalchemy_imperative   | 7.20 ms                                                | 9.10 ms: 1.26x slower                                                |
| unpickle_pure_python    | 159 us                                                 | 204 us: 1.28x slower                                                 |
| xml_etree_process       | 35.1 ms                                                | 45.0 ms: 1.28x slower                                                |
| pprint_safe_repr        | 466 ms                                                 | 600 ms: 1.29x slower                                                 |
| pprint_pformat          | 954 ms                                                 | 1.23 sec: 1.29x slower                                               |
| django_template         | 21.0 ms                                                | 27.2 ms: 1.29x slower                                                |
| tornado_http            | 71.5 ms                                                | 92.9 ms: 1.30x slower                                                |
| logging_simple          | 3.55 us                                                | 4.62 us: 1.30x slower                                                |
| deepcopy_memo           | 26.3 us                                                | 34.4 us: 1.31x slower                                                |
| pycparser               | 698 ms                                                 | 913 ms: 1.31x slower                                                 |
| logging_format          | 3.78 us                                                | 5.01 us: 1.33x slower                                                |
| spectral_norm           | 72.6 ms                                                | 96.3 ms: 1.33x slower                                                |
| thrift                  | 442 us                                                 | 586 us: 1.33x slower                                                 |
| hexiom                  | 4.72 ms                                                | 6.32 ms: 1.34x slower                                                |
| chaos                   | 49.4 ms                                                | 67.1 ms: 1.36x slower                                                |
| float                   | 53.0 ms                                                | 72.3 ms: 1.37x slower                                                |
| sqlglot_transpile       | 1.12 ms                                                | 1.54 ms: 1.37x slower                                                |
| html5lib                | 34.7 ms                                                | 47.8 ms: 1.38x slower                                                |
| sqlglot_parse           | 959 us                                                 | 1.33 ms: 1.39x slower                                                |
| async_tree_none         | 286 ms                                                 | 400 ms: 1.40x slower                                                 |
| pickle_pure_python      | 201 us                                                 | 287 us: 1.43x slower                                                 |
| nbody                   | 65.6 ms                                                | 94.1 ms: 1.43x slower                                                |
| async_tree_io           | 704 ms                                                 | 1.02 sec: 1.44x slower                                               |
| async_tree_memoization  | 336 ms                                                 | 488 ms: 1.45x slower                                                 |
| pyflate                 | 310 ms                                                 | 455 ms: 1.47x slower                                                 |
| scimark_lu              | 73.3 ms                                                | 110 ms: 1.50x slower                                                 |
| crypto_pyaes            | 51.7 ms                                                | 78.0 ms: 1.51x slower                                                |
| go                      | 109 ms                                                 | 165 ms: 1.52x slower                                                 |
| scimark_sor             | 82.6 ms                                                | 126 ms: 1.53x slower                                                 |
| richards                | 32.2 ms                                                | 50.2 ms: 1.56x slower                                                |
| scimark_monte_carlo     | 46.5 ms                                                | 72.8 ms: 1.57x slower                                                |
| mypy2                   | 195 ms                                                 | 308 ms: 1.58x slower                                                 |
| raytrace                | 207 ms                                                 | 330 ms: 1.60x slower                                                 |
| logging_silent          | 68.1 ns                                                | 118 ns: 1.73x slower                                                 |
| deltablue               | 2.81 ms                                                | 5.18 ms: 1.84x slower                                                |
| Geometric mean          | (ref)                                                  | 1.22x slower                                                         |
Ignored benchmarks (4) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230207-3.10.10-aad5f6a/bm-20230207-darwin-arm64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a.json: dask


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.20x
- 95% likely to have a slowdown of 1.19x
- 99% likely to have a slowdown of 1.17x
