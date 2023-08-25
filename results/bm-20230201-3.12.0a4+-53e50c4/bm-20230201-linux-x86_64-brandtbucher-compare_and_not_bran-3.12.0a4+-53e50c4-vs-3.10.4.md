
# Results vs. 3.10.4

- fork: brandtbucher
- ref: compare_and_not_bran
- machine: linux-x86_64
- commit hash: 53e50c4
- commit date: 2023-02-01
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 254 ms: 1.33x faster                                                         |
| chameleon      | 9.06 ms                                                | 6.44 ms: 1.41x faster                                                        |
| docutils       | 3.17 sec                                               | 2.55 sec: 1.25x faster                                                       |
| html5lib       | 85.9 ms                                                | 61.3 ms: 1.40x faster                                                        |
| tornado_http   | 127 ms                                                 | 94.1 ms: 1.35x faster                                                        |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.6 ms: 1.52x faster                                                        |
| nbody          | 142 ms                                                 | 93.7 ms: 1.51x faster                                                        |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 130 ms: 1.36x faster                                                         |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                        |
| regex_dna      | 222 ms                                                 | 210 ms: 1.06x faster                                                         |
| regex_effbot   | 3.23 ms                                                | 3.52 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 288 us: 1.58x faster                                                         |
| unpickle_pure_python | 300 us                                                 | 202 us: 1.48x faster                                                         |
| json_dumps           | 13.5 ms                                                | 9.62 ms: 1.41x faster                                                        |
| xml_etree_process    | 74.9 ms                                                | 54.1 ms: 1.39x faster                                                        |
| xml_etree_generate   | 94.2 ms                                                | 77.7 ms: 1.21x faster                                                        |
| json_loads           | 28.8 us                                                | 24.0 us: 1.20x faster                                                        |
| pickle_list          | 4.56 us                                                | 4.10 us: 1.11x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                         |
| unpickle             | 14.1 us                                                | 13.0 us: 1.09x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 105 ms: 1.06x faster                                                         |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                                        |
| unpickle_list        | 4.82 us                                                | 4.96 us: 1.03x slower                                                        |
| pickle_dict          | 27.3 us                                                | 30.7 us: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.89 ms: 1.59x faster                                                        |
| python_startup_no_site | 5.82 ms                                                | 6.44 ms: 1.11x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.20x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.69 ms: 1.52x faster                                                        |
| genshi_text     | 30.3 ms                                                | 20.4 ms: 1.48x faster                                                        |
| django_template | 45.9 ms                                                | 32.3 ms: 1.42x faster                                                        |
| genshi_xml      | 63.3 ms                                                | 46.6 ms: 1.36x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.21 ms: 2.31x faster                                                        |
| logging_silent          | 175 ns                                                 | 93.7 ns: 1.87x faster                                                        |
| asyncio_tcp             | 925 ms                                                 | 500 ms: 1.85x faster                                                         |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.82x faster                                                         |
| richards                | 74.9 ms                                                | 42.1 ms: 1.78x faster                                                        |
| pyflate                 | 673 ms                                                 | 400 ms: 1.68x faster                                                         |
| go                      | 229 ms                                                 | 137 ms: 1.68x faster                                                         |
| scimark_monte_carlo     | 108 ms                                                 | 65.0 ms: 1.67x faster                                                        |
| raytrace                | 464 ms                                                 | 281 ms: 1.65x faster                                                         |
| chaos                   | 106 ms                                                 | 65.0 ms: 1.64x faster                                                        |
| crypto_pyaes            | 118 ms                                                 | 72.9 ms: 1.62x faster                                                        |
| hexiom                  | 9.53 ms                                                | 5.89 ms: 1.62x faster                                                        |
| python_startup          | 14.2 ms                                                | 8.89 ms: 1.59x faster                                                        |
| spectral_norm           | 150 ms                                                 | 94.5 ms: 1.59x faster                                                        |
| pickle_pure_python      | 455 us                                                 | 288 us: 1.58x faster                                                         |
| scimark_lu              | 163 ms                                                 | 105 ms: 1.56x faster                                                         |
| mako                    | 14.8 ms                                                | 9.69 ms: 1.52x faster                                                        |
| float                   | 111 ms                                                 | 72.6 ms: 1.52x faster                                                        |
| nbody                   | 142 ms                                                 | 93.7 ms: 1.51x faster                                                        |
| deepcopy_memo           | 52.3 us                                                | 34.7 us: 1.51x faster                                                        |
| unpack_sequence         | 64.7 ns                                                | 43.6 ns: 1.49x faster                                                        |
| genshi_text             | 30.3 ms                                                | 20.4 ms: 1.48x faster                                                        |
| unpickle_pure_python    | 300 us                                                 | 202 us: 1.48x faster                                                         |
| sqlglot_parse           | 2.06 ms                                                | 1.42 ms: 1.45x faster                                                        |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.44x faster                                                       |
| sqlglot_transpile       | 2.45 ms                                                | 1.71 ms: 1.43x faster                                                        |
| django_template         | 45.9 ms                                                | 32.3 ms: 1.42x faster                                                        |
| pprint_safe_repr        | 955 ms                                                 | 675 ms: 1.42x faster                                                         |
| json_dumps              | 13.5 ms                                                | 9.62 ms: 1.41x faster                                                        |
| chameleon               | 9.06 ms                                                | 6.44 ms: 1.41x faster                                                        |
| scimark_fft             | 424 ms                                                 | 302 ms: 1.40x faster                                                         |
| html5lib                | 85.9 ms                                                | 61.3 ms: 1.40x faster                                                        |
| logging_format          | 8.91 us                                                | 6.38 us: 1.40x faster                                                        |
| logging_simple          | 8.07 us                                                | 5.78 us: 1.40x faster                                                        |
| aiohttp                 | 1.38 ms                                                | 995 us: 1.39x faster                                                         |
| thrift                  | 1.03 ms                                                | 744 us: 1.39x faster                                                         |
| xml_etree_process       | 74.9 ms                                                | 54.1 ms: 1.39x faster                                                        |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.37x faster                                                        |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.00 ms: 1.36x faster                                                        |
| regex_compile           | 177 ms                                                 | 130 ms: 1.36x faster                                                         |
| genshi_xml              | 63.3 ms                                                | 46.6 ms: 1.36x faster                                                        |
| tornado_http            | 127 ms                                                 | 94.1 ms: 1.35x faster                                                        |
| async_tree_none         | 717 ms                                                 | 530 ms: 1.35x faster                                                         |
| deepcopy                | 442 us                                                 | 329 us: 1.34x faster                                                         |
| async_tree_io           | 1.77 sec                                               | 1.33 sec: 1.34x faster                                                       |
| fannkuch                | 486 ms                                                 | 364 ms: 1.34x faster                                                         |
| 2to3                    | 336 ms                                                 | 254 ms: 1.33x faster                                                         |
| pycparser               | 1.50 sec                                               | 1.15 sec: 1.31x faster                                                       |
| deepcopy_reduce         | 3.82 us                                                | 2.93 us: 1.30x faster                                                        |
| async_tree_memoization  | 854 ms                                                 | 666 ms: 1.28x faster                                                         |
| sqlglot_optimize        | 65.3 ms                                                | 51.0 ms: 1.28x faster                                                        |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.28x faster                                                         |
| nqueens                 | 100 ms                                                 | 79.0 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed | 951 ms                                                 | 759 ms: 1.25x faster                                                         |
| coroutines              | 31.8 ms                                                | 25.5 ms: 1.25x faster                                                        |
| docutils                | 3.17 sec                                               | 2.55 sec: 1.25x faster                                                       |
| sympy_integrate         | 24.3 ms                                                | 19.7 ms: 1.23x faster                                                        |
| sympy_str               | 328 ms                                                 | 270 ms: 1.21x faster                                                         |
| xml_etree_generate      | 94.2 ms                                                | 77.7 ms: 1.21x faster                                                        |
| dulwich_log             | 75.9 ms                                                | 62.8 ms: 1.21x faster                                                        |
| bench_thread_pool       | 947 us                                                 | 787 us: 1.20x faster                                                         |
| async_generators        | 425 ms                                                 | 353 ms: 1.20x faster                                                         |
| sympy_expand            | 545 ms                                                 | 454 ms: 1.20x faster                                                         |
| json_loads              | 28.8 us                                                | 24.0 us: 1.20x faster                                                        |
| sympy_sum               | 185 ms                                                 | 155 ms: 1.19x faster                                                         |
| json                    | 5.42 ms                                                | 4.70 ms: 1.15x faster                                                        |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.15x faster                                                        |
| sqlite_synth            | 2.93 us                                                | 2.57 us: 1.14x faster                                                        |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                        |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                        |
| pickle_list             | 4.56 us                                                | 4.10 us: 1.11x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                         |
| djangocms               | 35.9 us                                                | 32.6 us: 1.10x faster                                                        |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                                         |
| mdp                     | 2.82 sec                                               | 2.58 sec: 1.09x faster                                                       |
| unpickle                | 14.1 us                                                | 13.0 us: 1.09x faster                                                        |
| xml_etree_iterparse     | 111 ms                                                 | 105 ms: 1.06x faster                                                         |
| regex_dna               | 222 ms                                                 | 210 ms: 1.06x faster                                                         |
| telco                   | 6.54 ms                                                | 6.40 ms: 1.02x faster                                                        |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                                        |
| generators              | 76.8 ms                                                | 76.5 ms: 1.00x faster                                                        |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                                         |
| bench_mp_pool           | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                        |
| unpickle_list           | 4.82 us                                                | 4.96 us: 1.03x slower                                                        |
| gc_traversal            | 3.84 ms                                                | 4.05 ms: 1.05x slower                                                        |
| regex_effbot            | 3.23 ms                                                | 3.52 ms: 1.09x slower                                                        |
| python_startup_no_site  | 5.82 ms                                                | 6.44 ms: 1.11x slower                                                        |
| pickle_dict             | 27.3 us                                                | 30.7 us: 1.13x slower                                                        |
| dask                    | 423 ms                                                 | 497 ms: 1.18x slower                                                         |
| coverage                | 72.8 ms                                                | 96.1 ms: 1.32x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                 |
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230201-3.12.0a4+-53e50c4/bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x
