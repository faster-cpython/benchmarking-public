
# Results vs. 3.10.4

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: fa5965d
- commit date: 2023-02-02
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                                       |
| chameleon      | 9.06 ms                                                | 6.26 ms: 1.45x faster                                                      |
| docutils       | 3.17 sec                                               | 2.49 sec: 1.27x faster                                                     |
| html5lib       | 85.9 ms                                                | 60.1 ms: 1.43x faster                                                      |
| tornado_http   | 127 ms                                                 | 94.3 ms: 1.35x faster                                                      |
| Geometric mean | (ref)                                                  | 1.37x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 111 ms                                                 | 71.9 ms: 1.54x faster                                                      |
| nbody          | 142 ms                                                 | 98.9 ms: 1.43x faster                                                      |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.28x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.39x faster                                                       |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.16x faster                                                      |
| regex_dna      | 222 ms                                                 | 210 ms: 1.05x faster                                                       |
| regex_effbot   | 3.23 ms                                                | 3.40 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                  | 1.13x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 285 us: 1.60x faster                                                       |
| unpickle_pure_python | 300 us                                                 | 198 us: 1.52x faster                                                       |
| json_dumps           | 13.5 ms                                                | 9.40 ms: 1.44x faster                                                      |
| xml_etree_process    | 74.9 ms                                                | 53.1 ms: 1.41x faster                                                      |
| xml_etree_generate   | 94.2 ms                                                | 76.7 ms: 1.23x faster                                                      |
| json_loads           | 28.8 us                                                | 23.9 us: 1.21x faster                                                      |
| pickle_list          | 4.56 us                                                | 4.15 us: 1.10x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                       |
| unpickle             | 14.1 us                                                | 13.1 us: 1.08x faster                                                      |
| unpickle_list        | 4.82 us                                                | 5.07 us: 1.05x slower                                                      |
| pickle_dict          | 27.3 us                                                | 31.0 us: 1.14x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                               |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.72 ms: 1.62x faster                                                      |
| python_startup_no_site | 5.82 ms                                                | 6.25 ms: 1.07x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.23x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.53 ms: 1.55x faster                                                      |
| genshi_text     | 30.3 ms                                                | 21.3 ms: 1.43x faster                                                      |
| django_template | 45.9 ms                                                | 32.9 ms: 1.39x faster                                                      |
| genshi_xml      | 63.3 ms                                                | 47.8 ms: 1.33x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.21 ms: 2.31x faster                                                      |
| logging_silent          | 175 ns                                                 | 92.0 ns: 1.90x faster                                                      |
| asyncio_tcp             | 925 ms                                                 | 496 ms: 1.87x faster                                                       |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                                       |
| richards                | 74.9 ms                                                | 42.2 ms: 1.77x faster                                                      |
| pyflate                 | 673 ms                                                 | 394 ms: 1.71x faster                                                       |
| go                      | 229 ms                                                 | 134 ms: 1.71x faster                                                       |
| scimark_monte_carlo     | 108 ms                                                 | 65.2 ms: 1.66x faster                                                      |
| chaos                   | 106 ms                                                 | 64.5 ms: 1.65x faster                                                      |
| raytrace                | 464 ms                                                 | 282 ms: 1.65x faster                                                       |
| python_startup          | 14.2 ms                                                | 8.72 ms: 1.62x faster                                                      |
| crypto_pyaes            | 118 ms                                                 | 73.1 ms: 1.62x faster                                                      |
| hexiom                  | 9.53 ms                                                | 5.93 ms: 1.61x faster                                                      |
| pickle_pure_python      | 455 us                                                 | 285 us: 1.60x faster                                                       |
| scimark_lu              | 163 ms                                                 | 105 ms: 1.56x faster                                                       |
| spectral_norm           | 150 ms                                                 | 96.8 ms: 1.55x faster                                                      |
| mako                    | 14.8 ms                                                | 9.53 ms: 1.55x faster                                                      |
| deepcopy_memo           | 52.3 us                                                | 34.0 us: 1.54x faster                                                      |
| float                   | 111 ms                                                 | 71.9 ms: 1.54x faster                                                      |
| unpickle_pure_python    | 300 us                                                 | 198 us: 1.52x faster                                                       |
| unpack_sequence         | 64.7 ns                                                | 43.5 ns: 1.49x faster                                                      |
| sqlglot_parse           | 2.06 ms                                                | 1.40 ms: 1.47x faster                                                      |
| chameleon               | 9.06 ms                                                | 6.26 ms: 1.45x faster                                                      |
| sqlglot_transpile       | 2.45 ms                                                | 1.69 ms: 1.45x faster                                                      |
| json_dumps              | 13.5 ms                                                | 9.40 ms: 1.44x faster                                                      |
| nbody                   | 142 ms                                                 | 98.9 ms: 1.43x faster                                                      |
| html5lib                | 85.9 ms                                                | 60.1 ms: 1.43x faster                                                      |
| genshi_text             | 30.3 ms                                                | 21.3 ms: 1.43x faster                                                      |
| pprint_pformat          | 1.99 sec                                               | 1.39 sec: 1.43x faster                                                     |
| pprint_safe_repr        | 955 ms                                                 | 676 ms: 1.41x faster                                                       |
| xml_etree_process       | 74.9 ms                                                | 53.1 ms: 1.41x faster                                                      |
| scimark_fft             | 424 ms                                                 | 304 ms: 1.39x faster                                                       |
| django_template         | 45.9 ms                                                | 32.9 ms: 1.39x faster                                                      |
| thrift                  | 1.03 ms                                                | 743 us: 1.39x faster                                                       |
| logging_format          | 8.91 us                                                | 6.42 us: 1.39x faster                                                      |
| regex_compile           | 177 ms                                                 | 128 ms: 1.39x faster                                                       |
| logging_simple          | 8.07 us                                                | 5.83 us: 1.38x faster                                                      |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                                      |
| async_tree_none         | 717 ms                                                 | 526 ms: 1.36x faster                                                       |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                                      |
| tornado_http            | 127 ms                                                 | 94.3 ms: 1.35x faster                                                      |
| fannkuch                | 486 ms                                                 | 361 ms: 1.35x faster                                                       |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                                       |
| deepcopy                | 442 us                                                 | 329 us: 1.34x faster                                                       |
| async_tree_io           | 1.77 sec                                               | 1.33 sec: 1.34x faster                                                     |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.08 ms: 1.34x faster                                                      |
| genshi_xml              | 63.3 ms                                                | 47.8 ms: 1.33x faster                                                      |
| nqueens                 | 100 ms                                                 | 75.8 ms: 1.32x faster                                                      |
| pycparser               | 1.50 sec                                               | 1.14 sec: 1.31x faster                                                     |
| deepcopy_reduce         | 3.82 us                                                | 2.91 us: 1.31x faster                                                      |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                       |
| sqlglot_optimize        | 65.3 ms                                                | 50.9 ms: 1.28x faster                                                      |
| async_tree_memoization  | 854 ms                                                 | 667 ms: 1.28x faster                                                       |
| docutils                | 3.17 sec                                               | 2.49 sec: 1.27x faster                                                     |
| async_tree_cpu_io_mixed | 951 ms                                                 | 755 ms: 1.26x faster                                                       |
| coroutines              | 31.8 ms                                                | 25.5 ms: 1.25x faster                                                      |
| xml_etree_generate      | 94.2 ms                                                | 76.7 ms: 1.23x faster                                                      |
| sympy_integrate         | 24.3 ms                                                | 19.8 ms: 1.23x faster                                                      |
| bench_thread_pool       | 947 us                                                 | 777 us: 1.22x faster                                                       |
| sympy_str               | 328 ms                                                 | 271 ms: 1.21x faster                                                       |
| json_loads              | 28.8 us                                                | 23.9 us: 1.21x faster                                                      |
| dulwich_log             | 75.9 ms                                                | 63.3 ms: 1.20x faster                                                      |
| async_generators        | 425 ms                                                 | 354 ms: 1.20x faster                                                       |
| sympy_expand            | 545 ms                                                 | 455 ms: 1.20x faster                                                       |
| sympy_sum               | 185 ms                                                 | 155 ms: 1.19x faster                                                       |
| json                    | 5.42 ms                                                | 4.60 ms: 1.18x faster                                                      |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.16x faster                                                      |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.14x faster                                                      |
| sqlite_synth            | 2.93 us                                                | 2.60 us: 1.13x faster                                                      |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                      |
| djangocms               | 35.9 us                                                | 32.4 us: 1.11x faster                                                      |
| mdp                     | 2.82 sec                                               | 2.56 sec: 1.10x faster                                                     |
| pickle_list             | 4.56 us                                                | 4.15 us: 1.10x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                       |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                       |
| meteor_contest          | 115 ms                                                 | 106 ms: 1.08x faster                                                       |
| unpickle                | 14.1 us                                                | 13.1 us: 1.08x faster                                                      |
| regex_dna               | 222 ms                                                 | 210 ms: 1.05x faster                                                       |
| telco                   | 6.54 ms                                                | 6.33 ms: 1.03x faster                                                      |
| generators              | 76.8 ms                                                | 78.1 ms: 1.02x slower                                                      |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                       |
| unpickle_list           | 4.82 us                                                | 5.07 us: 1.05x slower                                                      |
| regex_effbot            | 3.23 ms                                                | 3.40 ms: 1.05x slower                                                      |
| gc_traversal            | 3.84 ms                                                | 4.06 ms: 1.06x slower                                                      |
| python_startup_no_site  | 5.82 ms                                                | 6.25 ms: 1.07x slower                                                      |
| pickle_dict             | 27.3 us                                                | 31.0 us: 1.14x slower                                                      |
| dask                    | 423 ms                                                 | 499 ms: 1.18x slower                                                       |
| coverage                | 72.8 ms                                                | 99.5 ms: 1.37x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                               |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230202-3.12.0a4+-fa5965d/bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x
