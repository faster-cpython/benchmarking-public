
# Results vs. 3.10.4

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 866c937
- commit date: 2023-02-01
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                                       |
| chameleon      | 9.06 ms                                                | 6.41 ms: 1.41x faster                                                      |
| docutils       | 3.17 sec                                               | 2.50 sec: 1.27x faster                                                     |
| html5lib       | 85.9 ms                                                | 60.1 ms: 1.43x faster                                                      |
| tornado_http   | 127 ms                                                 | 94.5 ms: 1.35x faster                                                      |
| Geometric mean | (ref)                                                  | 1.36x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 94.9 ms: 1.49x faster                                                      |
| float          | 111 ms                                                 | 74.2 ms: 1.49x faster                                                      |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.29x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.38x faster                                                       |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                      |
| regex_dna      | 222 ms                                                 | 217 ms: 1.02x faster                                                       |
| regex_effbot   | 3.23 ms                                                | 3.76 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 283 us: 1.61x faster                                                       |
| unpickle_pure_python | 300 us                                                 | 200 us: 1.50x faster                                                       |
| json_dumps           | 13.5 ms                                                | 9.46 ms: 1.43x faster                                                      |
| xml_etree_process    | 74.9 ms                                                | 53.7 ms: 1.39x faster                                                      |
| xml_etree_generate   | 94.2 ms                                                | 78.0 ms: 1.21x faster                                                      |
| json_loads           | 28.8 us                                                | 24.3 us: 1.19x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                       |
| pickle_list          | 4.56 us                                                | 4.25 us: 1.07x faster                                                      |
| unpickle             | 14.1 us                                                | 13.3 us: 1.07x faster                                                      |
| unpickle_list        | 4.82 us                                                | 5.04 us: 1.05x slower                                                      |
| pickle_dict          | 27.3 us                                                | 32.4 us: 1.19x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                               |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.74 ms: 1.62x faster                                                      |
| python_startup_no_site | 5.82 ms                                                | 6.27 ms: 1.08x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.23x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.85 ms: 1.50x faster                                                      |
| genshi_text     | 30.3 ms                                                | 20.7 ms: 1.46x faster                                                      |
| django_template | 45.9 ms                                                | 33.0 ms: 1.39x faster                                                      |
| genshi_xml      | 63.3 ms                                                | 46.8 ms: 1.35x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.18 ms: 2.33x faster                                                      |
| logging_silent          | 175 ns                                                 | 90.6 ns: 1.93x faster                                                      |
| asyncio_tcp             | 925 ms                                                 | 497 ms: 1.86x faster                                                       |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.86x faster                                                       |
| richards                | 74.9 ms                                                | 41.9 ms: 1.79x faster                                                      |
| go                      | 229 ms                                                 | 133 ms: 1.72x faster                                                       |
| pyflate                 | 673 ms                                                 | 402 ms: 1.67x faster                                                       |
| scimark_monte_carlo     | 108 ms                                                 | 65.5 ms: 1.65x faster                                                      |
| chaos                   | 106 ms                                                 | 64.8 ms: 1.64x faster                                                      |
| raytrace                | 464 ms                                                 | 283 ms: 1.64x faster                                                       |
| python_startup          | 14.2 ms                                                | 8.74 ms: 1.62x faster                                                      |
| pickle_pure_python      | 455 us                                                 | 283 us: 1.61x faster                                                       |
| hexiom                  | 9.53 ms                                                | 5.96 ms: 1.60x faster                                                      |
| crypto_pyaes            | 118 ms                                                 | 74.2 ms: 1.60x faster                                                      |
| spectral_norm           | 150 ms                                                 | 96.9 ms: 1.55x faster                                                      |
| scimark_lu              | 163 ms                                                 | 106 ms: 1.54x faster                                                       |
| deepcopy_memo           | 52.3 us                                                | 34.3 us: 1.52x faster                                                      |
| unpack_sequence         | 64.7 ns                                                | 42.6 ns: 1.52x faster                                                      |
| unpickle_pure_python    | 300 us                                                 | 200 us: 1.50x faster                                                       |
| mako                    | 14.8 ms                                                | 9.85 ms: 1.50x faster                                                      |
| nbody                   | 142 ms                                                 | 94.9 ms: 1.49x faster                                                      |
| float                   | 111 ms                                                 | 74.2 ms: 1.49x faster                                                      |
| genshi_text             | 30.3 ms                                                | 20.7 ms: 1.46x faster                                                      |
| sqlglot_parse           | 2.06 ms                                                | 1.42 ms: 1.45x faster                                                      |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.43x faster                                                     |
| json_dumps              | 13.5 ms                                                | 9.46 ms: 1.43x faster                                                      |
| html5lib                | 85.9 ms                                                | 60.1 ms: 1.43x faster                                                      |
| sqlglot_transpile       | 2.45 ms                                                | 1.71 ms: 1.43x faster                                                      |
| pprint_safe_repr        | 955 ms                                                 | 670 ms: 1.43x faster                                                       |
| chameleon               | 9.06 ms                                                | 6.41 ms: 1.41x faster                                                      |
| logging_format          | 8.91 us                                                | 6.32 us: 1.41x faster                                                      |
| logging_simple          | 8.07 us                                                | 5.74 us: 1.41x faster                                                      |
| xml_etree_process       | 74.9 ms                                                | 53.7 ms: 1.39x faster                                                      |
| django_template         | 45.9 ms                                                | 33.0 ms: 1.39x faster                                                      |
| regex_compile           | 177 ms                                                 | 128 ms: 1.38x faster                                                       |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                                      |
| scimark_fft             | 424 ms                                                 | 307 ms: 1.38x faster                                                       |
| thrift                  | 1.03 ms                                                | 750 us: 1.38x faster                                                       |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.37x faster                                                      |
| async_tree_none         | 717 ms                                                 | 526 ms: 1.36x faster                                                       |
| deepcopy                | 442 us                                                 | 326 us: 1.36x faster                                                       |
| genshi_xml              | 63.3 ms                                                | 46.8 ms: 1.35x faster                                                      |
| tornado_http            | 127 ms                                                 | 94.5 ms: 1.35x faster                                                      |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.05 ms: 1.34x faster                                                      |
| fannkuch                | 486 ms                                                 | 362 ms: 1.34x faster                                                       |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                                       |
| async_tree_io           | 1.77 sec                                               | 1.33 sec: 1.34x faster                                                     |
| deepcopy_reduce         | 3.82 us                                                | 2.90 us: 1.32x faster                                                      |
| nqueens                 | 100 ms                                                 | 76.9 ms: 1.30x faster                                                      |
| pycparser               | 1.50 sec                                               | 1.16 sec: 1.30x faster                                                     |
| async_tree_memoization  | 854 ms                                                 | 661 ms: 1.29x faster                                                       |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.27x faster                                                       |
| sqlglot_optimize        | 65.3 ms                                                | 51.5 ms: 1.27x faster                                                      |
| docutils                | 3.17 sec                                               | 2.50 sec: 1.27x faster                                                     |
| async_tree_cpu_io_mixed | 951 ms                                                 | 758 ms: 1.25x faster                                                       |
| sympy_integrate         | 24.3 ms                                                | 19.6 ms: 1.24x faster                                                      |
| sympy_str               | 328 ms                                                 | 269 ms: 1.22x faster                                                       |
| coroutines              | 31.8 ms                                                | 26.2 ms: 1.22x faster                                                      |
| dulwich_log             | 75.9 ms                                                | 62.8 ms: 1.21x faster                                                      |
| bench_thread_pool       | 947 us                                                 | 785 us: 1.21x faster                                                       |
| xml_etree_generate      | 94.2 ms                                                | 78.0 ms: 1.21x faster                                                      |
| sympy_expand            | 545 ms                                                 | 452 ms: 1.21x faster                                                       |
| async_generators        | 425 ms                                                 | 353 ms: 1.20x faster                                                       |
| sympy_sum               | 185 ms                                                 | 155 ms: 1.19x faster                                                       |
| json_loads              | 28.8 us                                                | 24.3 us: 1.19x faster                                                      |
| json                    | 5.42 ms                                                | 4.69 ms: 1.16x faster                                                      |
| sqlite_synth            | 2.93 us                                                | 2.58 us: 1.14x faster                                                      |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.13x faster                                                      |
| mdp                     | 2.82 sec                                               | 2.51 sec: 1.12x faster                                                     |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                      |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                       |
| djangocms               | 35.9 us                                                | 32.6 us: 1.10x faster                                                      |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.09x faster                                                       |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                                       |
| pickle_list             | 4.56 us                                                | 4.25 us: 1.07x faster                                                      |
| unpickle                | 14.1 us                                                | 13.3 us: 1.07x faster                                                      |
| regex_dna               | 222 ms                                                 | 217 ms: 1.02x faster                                                       |
| generators              | 76.8 ms                                                | 76.0 ms: 1.01x faster                                                      |
| gc_traversal            | 3.84 ms                                                | 3.82 ms: 1.00x faster                                                      |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                       |
| unpickle_list           | 4.82 us                                                | 5.04 us: 1.05x slower                                                      |
| python_startup_no_site  | 5.82 ms                                                | 6.27 ms: 1.08x slower                                                      |
| regex_effbot            | 3.23 ms                                                | 3.76 ms: 1.17x slower                                                      |
| dask                    | 423 ms                                                 | 501 ms: 1.19x slower                                                       |
| pickle_dict             | 27.3 us                                                | 32.4 us: 1.19x slower                                                      |
| coverage                | 72.8 ms                                                | 100 ms: 1.37x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                               |

Benchmark hidden because not significant (3): pickle, telco, bench_mp_pool
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230201-3.12.0a4+-866c937/bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.26x
