
# Results vs. 3.10.4

- fork: brandtbucher
- ref: compare_and_not_bran
- machine: linux-x86_64
- commit hash: 39ace64
- commit date: 2023-02-22
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 249 ms: 1.35x faster                                                         |
| chameleon      | 9.06 ms                                                | 6.43 ms: 1.41x faster                                                        |
| docutils       | 3.17 sec                                               | 2.55 sec: 1.24x faster                                                       |
| html5lib       | 85.9 ms                                                | 61.8 ms: 1.39x faster                                                        |
| tornado_http   | 127 ms                                                 | 94.5 ms: 1.35x faster                                                        |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                 | 73.4 ms: 1.51x faster                                                        |
| nbody          | 142 ms                                                 | 96.7 ms: 1.46x faster                                                        |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.38x faster                                                         |
| regex_v8       | 25.0 ms                                                | 22.0 ms: 1.14x faster                                                        |
| regex_dna      | 222 ms                                                 | 216 ms: 1.03x faster                                                         |
| regex_effbot   | 3.23 ms                                                | 3.52 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 286 us: 1.59x faster                                                         |
| unpickle_pure_python | 300 us                                                 | 198 us: 1.51x faster                                                         |
| json_dumps           | 13.5 ms                                                | 9.43 ms: 1.44x faster                                                        |
| xml_etree_process    | 74.9 ms                                                | 54.6 ms: 1.37x faster                                                        |
| json_loads           | 28.8 us                                                | 24.0 us: 1.20x faster                                                        |
| xml_etree_generate   | 94.2 ms                                                | 80.4 ms: 1.17x faster                                                        |
| pickle_list          | 4.56 us                                                | 4.03 us: 1.13x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 99.5 ms: 1.12x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 150 ms: 1.08x faster                                                         |
| unpickle             | 14.1 us                                                | 13.6 us: 1.04x faster                                                        |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                                        |
| unpickle_list        | 4.82 us                                                | 5.02 us: 1.04x slower                                                        |
| pickle_dict          | 27.3 us                                                | 30.9 us: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.02 ms: 1.57x faster                                                        |
| python_startup_no_site | 5.82 ms                                                | 6.54 ms: 1.12x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.80 ms: 1.51x faster                                                        |
| genshi_text     | 30.3 ms                                                | 20.7 ms: 1.46x faster                                                        |
| django_template | 45.9 ms                                                | 32.6 ms: 1.41x faster                                                        |
| genshi_xml      | 63.3 ms                                                | 46.7 ms: 1.36x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.6 ms: 2.60x faster                                                        |
| deltablue               | 7.42 ms                                                | 3.14 ms: 2.36x faster                                                        |
| logging_silent          | 175 ns                                                 | 90.4 ns: 1.94x faster                                                        |
| asyncio_tcp             | 925 ms                                                 | 501 ms: 1.85x faster                                                         |
| scimark_sor             | 197 ms                                                 | 109 ms: 1.81x faster                                                         |
| richards                | 74.9 ms                                                | 42.4 ms: 1.77x faster                                                        |
| go                      | 229 ms                                                 | 137 ms: 1.67x faster                                                         |
| raytrace                | 464 ms                                                 | 283 ms: 1.64x faster                                                         |
| pyflate                 | 673 ms                                                 | 412 ms: 1.64x faster                                                         |
| scimark_monte_carlo     | 108 ms                                                 | 66.2 ms: 1.63x faster                                                        |
| crypto_pyaes            | 118 ms                                                 | 73.1 ms: 1.62x faster                                                        |
| hexiom                  | 9.53 ms                                                | 5.90 ms: 1.61x faster                                                        |
| pickle_pure_python      | 455 us                                                 | 286 us: 1.59x faster                                                         |
| chaos                   | 106 ms                                                 | 67.0 ms: 1.59x faster                                                        |
| spectral_norm           | 150 ms                                                 | 95.4 ms: 1.57x faster                                                        |
| python_startup          | 14.2 ms                                                | 9.02 ms: 1.57x faster                                                        |
| deepcopy_memo           | 52.3 us                                                | 34.1 us: 1.53x faster                                                        |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.53x faster                                                         |
| unpack_sequence         | 64.7 ns                                                | 42.4 ns: 1.52x faster                                                        |
| unpickle_pure_python    | 300 us                                                 | 198 us: 1.51x faster                                                         |
| float                   | 111 ms                                                 | 73.4 ms: 1.51x faster                                                        |
| mako                    | 14.8 ms                                                | 9.80 ms: 1.51x faster                                                        |
| sqlglot_parse           | 2.06 ms                                                | 1.39 ms: 1.48x faster                                                        |
| genshi_text             | 30.3 ms                                                | 20.7 ms: 1.46x faster                                                        |
| nbody                   | 142 ms                                                 | 96.7 ms: 1.46x faster                                                        |
| sqlglot_transpile       | 2.45 ms                                                | 1.68 ms: 1.46x faster                                                        |
| json_dumps              | 13.5 ms                                                | 9.43 ms: 1.44x faster                                                        |
| pprint_pformat          | 1.99 sec                                               | 1.40 sec: 1.42x faster                                                       |
| coroutines              | 31.8 ms                                                | 22.4 ms: 1.42x faster                                                        |
| chameleon               | 9.06 ms                                                | 6.43 ms: 1.41x faster                                                        |
| django_template         | 45.9 ms                                                | 32.6 ms: 1.41x faster                                                        |
| logging_format          | 8.91 us                                                | 6.36 us: 1.40x faster                                                        |
| logging_simple          | 8.07 us                                                | 5.80 us: 1.39x faster                                                        |
| html5lib                | 85.9 ms                                                | 61.8 ms: 1.39x faster                                                        |
| pprint_safe_repr        | 955 ms                                                 | 688 ms: 1.39x faster                                                         |
| regex_compile           | 177 ms                                                 | 128 ms: 1.38x faster                                                         |
| pycparser               | 1.50 sec                                               | 1.09 sec: 1.38x faster                                                       |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                        |
| xml_etree_process       | 74.9 ms                                                | 54.6 ms: 1.37x faster                                                        |
| scimark_fft             | 424 ms                                                 | 309 ms: 1.37x faster                                                         |
| async_tree_none         | 717 ms                                                 | 527 ms: 1.36x faster                                                         |
| thrift                  | 1.03 ms                                                | 761 us: 1.36x faster                                                         |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.02 ms: 1.36x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 1.31 sec: 1.36x faster                                                       |
| genshi_xml              | 63.3 ms                                                | 46.7 ms: 1.36x faster                                                        |
| tornado_http            | 127 ms                                                 | 94.5 ms: 1.35x faster                                                        |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                                        |
| 2to3                    | 336 ms                                                 | 249 ms: 1.35x faster                                                         |
| deepcopy                | 442 us                                                 | 330 us: 1.34x faster                                                         |
| fannkuch                | 486 ms                                                 | 364 ms: 1.34x faster                                                         |
| sqlglot_normalize       | 135 ms                                                 | 102 ms: 1.32x faster                                                         |
| deepcopy_reduce         | 3.82 us                                                | 2.93 us: 1.30x faster                                                        |
| sqlglot_optimize        | 65.3 ms                                                | 50.2 ms: 1.30x faster                                                        |
| mypy2                   | 428 ms                                                 | 332 ms: 1.29x faster                                                         |
| async_tree_memoization  | 854 ms                                                 | 666 ms: 1.28x faster                                                         |
| nqueens                 | 100 ms                                                 | 78.1 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed | 951 ms                                                 | 744 ms: 1.28x faster                                                         |
| docutils                | 3.17 sec                                               | 2.55 sec: 1.24x faster                                                       |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.21x faster                                                         |
| dulwich_log             | 75.9 ms                                                | 62.9 ms: 1.21x faster                                                        |
| json_loads              | 28.8 us                                                | 24.0 us: 1.20x faster                                                        |
| bench_thread_pool       | 947 us                                                 | 790 us: 1.20x faster                                                         |
| sympy_expand            | 545 ms                                                 | 455 ms: 1.20x faster                                                         |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                                        |
| json                    | 5.42 ms                                                | 4.58 ms: 1.18x faster                                                        |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.9 ms: 1.18x faster                                                        |
| xml_etree_generate      | 94.2 ms                                                | 80.4 ms: 1.17x faster                                                        |
| sympy_str               | 328 ms                                                 | 284 ms: 1.16x faster                                                         |
| regex_v8                | 25.0 ms                                                | 22.0 ms: 1.14x faster                                                        |
| pickle_list             | 4.56 us                                                | 4.03 us: 1.13x faster                                                        |
| sqlite_synth            | 2.93 us                                                | 2.61 us: 1.13x faster                                                        |
| xml_etree_iterparse     | 111 ms                                                 | 99.5 ms: 1.12x faster                                                        |
| mdp                     | 2.82 sec                                               | 2.52 sec: 1.12x faster                                                       |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.12x faster                                                         |
| create_gc_cycles        | 1.67 ms                                                | 1.50 ms: 1.12x faster                                                        |
| sympy_sum               | 185 ms                                                 | 165 ms: 1.12x faster                                                         |
| pathlib                 | 20.0 ms                                                | 18.1 ms: 1.11x faster                                                        |
| djangocms               | 35.9 us                                                | 32.6 us: 1.10x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 150 ms: 1.08x faster                                                         |
| unpickle                | 14.1 us                                                | 13.6 us: 1.04x faster                                                        |
| async_generators        | 425 ms                                                 | 409 ms: 1.04x faster                                                         |
| regex_dna               | 222 ms                                                 | 216 ms: 1.03x faster                                                         |
| telco                   | 6.54 ms                                                | 6.39 ms: 1.02x faster                                                        |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                                        |
| bench_mp_pool           | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                        |
| gc_traversal            | 3.84 ms                                                | 3.85 ms: 1.00x slower                                                        |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                                         |
| unpickle_list           | 4.82 us                                                | 5.02 us: 1.04x slower                                                        |
| regex_effbot            | 3.23 ms                                                | 3.52 ms: 1.09x slower                                                        |
| python_startup_no_site  | 5.82 ms                                                | 6.54 ms: 1.12x slower                                                        |
| pickle_dict             | 27.3 us                                                | 30.9 us: 1.13x slower                                                        |
| dask                    | 423 ms                                                 | 503 ms: 1.19x slower                                                         |
| coverage                | 72.8 ms                                                | 98.2 ms: 1.35x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                                 |
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x
