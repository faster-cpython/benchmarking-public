
# Results vs. 3.10.4

- fork: brandtbucher
- ref: type_cache_fixed_lar
- machine: linux-x86_64
- commit hash: cc70763
- commit date: 2023-03-23
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                                         |
| chameleon      | 9.06 ms                                                | 6.38 ms: 1.42x faster                                                        |
| docutils       | 3.17 sec                                               | 2.52 sec: 1.26x faster                                                       |
| html5lib       | 85.9 ms                                                | 61.3 ms: 1.40x faster                                                        |
| tornado_http   | 127 ms                                                 | 91.2 ms: 1.40x faster                                                        |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 87.7 ms: 1.61x faster                                                        |
| float          | 111 ms                                                 | 72.5 ms: 1.52x faster                                                        |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 133 ms: 1.33x faster                                                         |
| regex_v8       | 25.0 ms                                                | 21.3 ms: 1.18x faster                                                        |
| regex_dna      | 222 ms                                                 | 206 ms: 1.08x faster                                                         |
| regex_effbot   | 3.23 ms                                                | 3.42 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 286 us: 1.59x faster                                                         |
| unpickle_pure_python | 300 us                                                 | 199 us: 1.51x faster                                                         |
| json_dumps           | 13.5 ms                                                | 9.55 ms: 1.42x faster                                                        |
| xml_etree_process    | 74.9 ms                                                | 56.2 ms: 1.33x faster                                                        |
| json_loads           | 28.8 us                                                | 23.8 us: 1.21x faster                                                        |
| xml_etree_generate   | 94.2 ms                                                | 80.6 ms: 1.17x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 99.9 ms: 1.12x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                         |
| unpickle             | 14.1 us                                                | 13.3 us: 1.06x faster                                                        |
| pickle_list          | 4.56 us                                                | 4.36 us: 1.04x faster                                                        |
| pickle               | 10.3 us                                                | 10.6 us: 1.03x slower                                                        |
| unpickle_list        | 4.82 us                                                | 5.09 us: 1.06x slower                                                        |
| pickle_dict          | 27.3 us                                                | 31.7 us: 1.16x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.85 ms: 1.60x faster                                                        |
| python_startup_no_site | 5.82 ms                                                | 6.55 ms: 1.13x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.00 ms: 1.48x faster                                                       |
| genshi_text     | 30.3 ms                                                | 21.2 ms: 1.43x faster                                                        |
| django_template | 45.9 ms                                                | 33.1 ms: 1.39x faster                                                        |
| genshi_xml      | 63.3 ms                                                | 47.2 ms: 1.34x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.8 ms: 2.58x faster                                                        |
| deltablue               | 7.42 ms                                                | 3.30 ms: 2.25x faster                                                        |
| asyncio_tcp             | 925 ms                                                 | 509 ms: 1.82x faster                                                         |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.82x faster                                                         |
| logging_silent          | 175 ns                                                 | 97.2 ns: 1.80x faster                                                        |
| richards                | 74.9 ms                                                | 44.2 ms: 1.69x faster                                                        |
| scimark_monte_carlo     | 108 ms                                                 | 65.8 ms: 1.64x faster                                                        |
| go                      | 229 ms                                                 | 140 ms: 1.64x faster                                                         |
| raytrace                | 464 ms                                                 | 285 ms: 1.62x faster                                                         |
| pyflate                 | 673 ms                                                 | 415 ms: 1.62x faster                                                         |
| nbody                   | 142 ms                                                 | 87.7 ms: 1.61x faster                                                        |
| chaos                   | 106 ms                                                 | 66.2 ms: 1.60x faster                                                        |
| python_startup          | 14.2 ms                                                | 8.85 ms: 1.60x faster                                                        |
| pickle_pure_python      | 455 us                                                 | 286 us: 1.59x faster                                                         |
| crypto_pyaes            | 118 ms                                                 | 75.0 ms: 1.58x faster                                                        |
| spectral_norm           | 150 ms                                                 | 95.0 ms: 1.58x faster                                                        |
| hexiom                  | 9.53 ms                                                | 6.09 ms: 1.56x faster                                                        |
| float                   | 111 ms                                                 | 72.5 ms: 1.52x faster                                                        |
| deepcopy_memo           | 52.3 us                                                | 34.6 us: 1.51x faster                                                        |
| unpickle_pure_python    | 300 us                                                 | 199 us: 1.51x faster                                                         |
| scimark_lu              | 163 ms                                                 | 109 ms: 1.50x faster                                                         |
| mako                    | 14.8 ms                                                | 10.00 ms: 1.48x faster                                                       |
| genshi_text             | 30.3 ms                                                | 21.2 ms: 1.43x faster                                                        |
| sqlglot_parse           | 2.06 ms                                                | 1.45 ms: 1.42x faster                                                        |
| chameleon               | 9.06 ms                                                | 6.38 ms: 1.42x faster                                                        |
| json_dumps              | 13.5 ms                                                | 9.55 ms: 1.42x faster                                                        |
| unpack_sequence         | 64.7 ns                                                | 45.9 ns: 1.41x faster                                                        |
| sqlglot_transpile       | 2.45 ms                                                | 1.74 ms: 1.41x faster                                                        |
| pprint_pformat          | 1.99 sec                                               | 1.41 sec: 1.40x faster                                                       |
| html5lib                | 85.9 ms                                                | 61.3 ms: 1.40x faster                                                        |
| tornado_http            | 127 ms                                                 | 91.2 ms: 1.40x faster                                                        |
| django_template         | 45.9 ms                                                | 33.1 ms: 1.39x faster                                                        |
| scimark_fft             | 424 ms                                                 | 305 ms: 1.39x faster                                                         |
| pprint_safe_repr        | 955 ms                                                 | 691 ms: 1.38x faster                                                         |
| async_tree_none         | 717 ms                                                 | 521 ms: 1.38x faster                                                         |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.37x faster                                                       |
| logging_format          | 8.91 us                                                | 6.50 us: 1.37x faster                                                        |
| logging_simple          | 8.07 us                                                | 5.91 us: 1.36x faster                                                        |
| pycparser               | 1.50 sec                                               | 1.10 sec: 1.36x faster                                                       |
| deepcopy                | 442 us                                                 | 325 us: 1.36x faster                                                         |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.05 ms: 1.35x faster                                                        |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                                        |
| coroutines              | 31.8 ms                                                | 23.7 ms: 1.34x faster                                                        |
| genshi_xml              | 63.3 ms                                                | 47.2 ms: 1.34x faster                                                        |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                                         |
| thrift                  | 1.03 ms                                                | 775 us: 1.33x faster                                                         |
| xml_etree_process       | 74.9 ms                                                | 56.2 ms: 1.33x faster                                                        |
| regex_compile           | 177 ms                                                 | 133 ms: 1.33x faster                                                         |
| fannkuch                | 486 ms                                                 | 366 ms: 1.33x faster                                                         |
| async_tree_memoization  | 854 ms                                                 | 655 ms: 1.30x faster                                                         |
| deepcopy_reduce         | 3.82 us                                                | 2.94 us: 1.30x faster                                                        |
| async_tree_cpu_io_mixed | 951 ms                                                 | 738 ms: 1.29x faster                                                         |
| mypy2                   | 428 ms                                                 | 333 ms: 1.29x faster                                                         |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.27x faster                                                         |
| sqlglot_optimize        | 65.3 ms                                                | 51.6 ms: 1.27x faster                                                        |
| docutils                | 3.17 sec                                               | 2.52 sec: 1.26x faster                                                       |
| nqueens                 | 100 ms                                                 | 79.9 ms: 1.25x faster                                                        |
| json_loads              | 28.8 us                                                | 23.8 us: 1.21x faster                                                        |
| dulwich_log             | 75.9 ms                                                | 63.0 ms: 1.20x faster                                                        |
| bench_thread_pool       | 947 us                                                 | 789 us: 1.20x faster                                                         |
| sympy_expand            | 545 ms                                                 | 458 ms: 1.19x faster                                                         |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                                        |
| regex_v8                | 25.0 ms                                                | 21.3 ms: 1.18x faster                                                        |
| json                    | 5.42 ms                                                | 4.61 ms: 1.18x faster                                                        |
| xml_etree_generate      | 94.2 ms                                                | 80.6 ms: 1.17x faster                                                        |
| sympy_str               | 328 ms                                                 | 282 ms: 1.16x faster                                                         |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.13x faster                                                        |
| comprehensions          | 26.8 us                                                | 23.8 us: 1.13x faster                                                        |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                        |
| sympy_sum               | 185 ms                                                 | 165 ms: 1.12x faster                                                         |
| xml_etree_iterparse     | 111 ms                                                 | 99.9 ms: 1.12x faster                                                        |
| sqlite_synth            | 2.93 us                                                | 2.63 us: 1.11x faster                                                        |
| djangocms               | 35.9 us                                                | 32.3 us: 1.11x faster                                                        |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.11x faster                                                         |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                         |
| regex_dna               | 222 ms                                                 | 206 ms: 1.08x faster                                                         |
| unpickle                | 14.1 us                                                | 13.3 us: 1.06x faster                                                        |
| mdp                     | 2.82 sec                                               | 2.69 sec: 1.05x faster                                                       |
| gc_traversal            | 3.84 ms                                                | 3.67 ms: 1.05x faster                                                        |
| pickle_list             | 4.56 us                                                | 4.36 us: 1.04x faster                                                        |
| async_generators        | 425 ms                                                 | 413 ms: 1.03x faster                                                         |
| telco                   | 6.54 ms                                                | 6.49 ms: 1.01x faster                                                        |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                         |
| bench_mp_pool           | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                        |
| pickle                  | 10.3 us                                                | 10.6 us: 1.03x slower                                                        |
| unpickle_list           | 4.82 us                                                | 5.09 us: 1.06x slower                                                        |
| regex_effbot            | 3.23 ms                                                | 3.42 ms: 1.06x slower                                                        |
| python_startup_no_site  | 5.82 ms                                                | 6.55 ms: 1.13x slower                                                        |
| pickle_dict             | 27.3 us                                                | 31.7 us: 1.16x slower                                                        |
| dask                    | 423 ms                                                 | 505 ms: 1.20x slower                                                         |
| coverage                | 72.8 ms                                                | 93.0 ms: 1.28x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                 |
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x
