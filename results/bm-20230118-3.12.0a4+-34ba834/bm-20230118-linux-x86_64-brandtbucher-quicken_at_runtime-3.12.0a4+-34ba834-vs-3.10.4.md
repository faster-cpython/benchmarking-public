
# Results vs. 3.10.4

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 34ba834
- commit date: 2023-01-18
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 256 ms: 1.32x faster                                                       |
| chameleon      | 9.06 ms                                                | 6.56 ms: 1.38x faster                                                      |
| docutils       | 3.17 sec                                               | 2.50 sec: 1.27x faster                                                     |
| html5lib       | 85.9 ms                                                | 61.4 ms: 1.40x faster                                                      |
| tornado_http   | 127 ms                                                 | 94.7 ms: 1.34x faster                                                      |
| Geometric mean | (ref)                                                  | 1.34x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 92.5 ms: 1.53x faster                                                      |
| float          | 111 ms                                                 | 74.3 ms: 1.49x faster                                                      |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.30x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 130 ms: 1.36x faster                                                       |
| regex_v8       | 25.0 ms                                                | 21.1 ms: 1.19x faster                                                      |
| regex_dna      | 222 ms                                                 | 201 ms: 1.10x faster                                                       |
| regex_effbot   | 3.23 ms                                                | 3.44 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                  | 1.14x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 290 us: 1.57x faster                                                       |
| unpickle_pure_python | 300 us                                                 | 209 us: 1.44x faster                                                       |
| json_dumps           | 13.5 ms                                                | 9.55 ms: 1.42x faster                                                      |
| xml_etree_process    | 74.9 ms                                                | 53.5 ms: 1.40x faster                                                      |
| xml_etree_generate   | 94.2 ms                                                | 77.2 ms: 1.22x faster                                                      |
| json_loads           | 28.8 us                                                | 24.4 us: 1.18x faster                                                      |
| pickle_list          | 4.56 us                                                | 4.02 us: 1.13x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                       |
| unpickle             | 14.1 us                                                | 13.3 us: 1.06x faster                                                      |
| pickle               | 10.3 us                                                | 10.0 us: 1.03x faster                                                      |
| unpickle_list        | 4.82 us                                                | 4.99 us: 1.04x slower                                                      |
| pickle_dict          | 27.3 us                                                | 30.6 us: 1.12x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.72 ms: 1.62x faster                                                      |
| python_startup_no_site | 5.82 ms                                                | 6.25 ms: 1.07x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.23x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.57 ms: 1.54x faster                                                      |
| genshi_text     | 30.3 ms                                                | 20.5 ms: 1.48x faster                                                      |
| django_template | 45.9 ms                                                | 32.7 ms: 1.40x faster                                                      |
| genshi_xml      | 63.3 ms                                                | 48.1 ms: 1.32x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.32 ms: 2.24x faster                                                      |
| logging_silent          | 175 ns                                                 | 92.3 ns: 1.90x faster                                                      |
| asyncio_tcp             | 925 ms                                                 | 491 ms: 1.88x faster                                                       |
| richards                | 74.9 ms                                                | 43.8 ms: 1.71x faster                                                      |
| go                      | 229 ms                                                 | 139 ms: 1.65x faster                                                       |
| raytrace                | 464 ms                                                 | 282 ms: 1.65x faster                                                       |
| crypto_pyaes            | 118 ms                                                 | 72.8 ms: 1.63x faster                                                      |
| chaos                   | 106 ms                                                 | 65.3 ms: 1.63x faster                                                      |
| python_startup          | 14.2 ms                                                | 8.72 ms: 1.62x faster                                                      |
| scimark_sor             | 197 ms                                                 | 121 ms: 1.62x faster                                                       |
| scimark_monte_carlo     | 108 ms                                                 | 67.6 ms: 1.60x faster                                                      |
| pyflate                 | 673 ms                                                 | 421 ms: 1.60x faster                                                       |
| spectral_norm           | 150 ms                                                 | 95.4 ms: 1.57x faster                                                      |
| pickle_pure_python      | 455 us                                                 | 290 us: 1.57x faster                                                       |
| hexiom                  | 9.53 ms                                                | 6.12 ms: 1.56x faster                                                      |
| mako                    | 14.8 ms                                                | 9.57 ms: 1.54x faster                                                      |
| deepcopy_memo           | 52.3 us                                                | 34.0 us: 1.54x faster                                                      |
| nbody                   | 142 ms                                                 | 92.5 ms: 1.53x faster                                                      |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.53x faster                                                       |
| unpack_sequence         | 64.7 ns                                                | 43.3 ns: 1.49x faster                                                      |
| float                   | 111 ms                                                 | 74.3 ms: 1.49x faster                                                      |
| genshi_text             | 30.3 ms                                                | 20.5 ms: 1.48x faster                                                      |
| sqlglot_parse           | 2.06 ms                                                | 1.41 ms: 1.46x faster                                                      |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.44x faster                                                     |
| sqlglot_transpile       | 2.45 ms                                                | 1.70 ms: 1.44x faster                                                      |
| unpickle_pure_python    | 300 us                                                 | 209 us: 1.44x faster                                                       |
| json_dumps              | 13.5 ms                                                | 9.55 ms: 1.42x faster                                                      |
| pprint_safe_repr        | 955 ms                                                 | 677 ms: 1.41x faster                                                       |
| django_template         | 45.9 ms                                                | 32.7 ms: 1.40x faster                                                      |
| xml_etree_process       | 74.9 ms                                                | 53.5 ms: 1.40x faster                                                      |
| html5lib                | 85.9 ms                                                | 61.4 ms: 1.40x faster                                                      |
| thrift                  | 1.03 ms                                                | 741 us: 1.39x faster                                                       |
| scimark_fft             | 424 ms                                                 | 305 ms: 1.39x faster                                                       |
| logging_format          | 8.91 us                                                | 6.42 us: 1.39x faster                                                      |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                                      |
| chameleon               | 9.06 ms                                                | 6.56 ms: 1.38x faster                                                      |
| logging_simple          | 8.07 us                                                | 5.85 us: 1.38x faster                                                      |
| async_tree_none         | 717 ms                                                 | 526 ms: 1.36x faster                                                       |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.36x faster                                                      |
| regex_compile           | 177 ms                                                 | 130 ms: 1.36x faster                                                       |
| async_tree_io           | 1.77 sec                                               | 1.31 sec: 1.35x faster                                                     |
| pycparser               | 1.50 sec                                               | 1.11 sec: 1.35x faster                                                     |
| tornado_http            | 127 ms                                                 | 94.7 ms: 1.34x faster                                                      |
| deepcopy                | 442 us                                                 | 329 us: 1.34x faster                                                       |
| genshi_xml              | 63.3 ms                                                | 48.1 ms: 1.32x faster                                                      |
| 2to3                    | 336 ms                                                 | 256 ms: 1.32x faster                                                       |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.16 ms: 1.31x faster                                                      |
| async_tree_memoization  | 854 ms                                                 | 659 ms: 1.30x faster                                                       |
| deepcopy_reduce         | 3.82 us                                                | 2.96 us: 1.29x faster                                                      |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                       |
| fannkuch                | 486 ms                                                 | 378 ms: 1.29x faster                                                       |
| sqlglot_optimize        | 65.3 ms                                                | 50.8 ms: 1.29x faster                                                      |
| nqueens                 | 100 ms                                                 | 78.7 ms: 1.27x faster                                                      |
| docutils                | 3.17 sec                                               | 2.50 sec: 1.27x faster                                                     |
| async_tree_cpu_io_mixed | 951 ms                                                 | 756 ms: 1.26x faster                                                       |
| coroutines              | 31.8 ms                                                | 25.8 ms: 1.23x faster                                                      |
| xml_etree_generate      | 94.2 ms                                                | 77.2 ms: 1.22x faster                                                      |
| sympy_integrate         | 24.3 ms                                                | 20.0 ms: 1.22x faster                                                      |
| sympy_str               | 328 ms                                                 | 271 ms: 1.21x faster                                                       |
| dulwich_log             | 75.9 ms                                                | 62.9 ms: 1.21x faster                                                      |
| bench_thread_pool       | 947 us                                                 | 791 us: 1.20x faster                                                       |
| sympy_expand            | 545 ms                                                 | 455 ms: 1.20x faster                                                       |
| regex_v8                | 25.0 ms                                                | 21.1 ms: 1.19x faster                                                      |
| sympy_sum               | 185 ms                                                 | 156 ms: 1.18x faster                                                       |
| async_generators        | 425 ms                                                 | 359 ms: 1.18x faster                                                       |
| json_loads              | 28.8 us                                                | 24.4 us: 1.18x faster                                                      |
| json                    | 5.42 ms                                                | 4.67 ms: 1.16x faster                                                      |
| create_gc_cycles        | 1.67 ms                                                | 1.45 ms: 1.15x faster                                                      |
| pickle_list             | 4.56 us                                                | 4.02 us: 1.13x faster                                                      |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.13x faster                                                      |
| sqlite_synth            | 2.93 us                                                | 2.61 us: 1.12x faster                                                      |
| djangocms               | 35.9 us                                                | 32.4 us: 1.11x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                       |
| regex_dna               | 222 ms                                                 | 201 ms: 1.10x faster                                                       |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                       |
| meteor_contest          | 115 ms                                                 | 106 ms: 1.09x faster                                                       |
| mdp                     | 2.82 sec                                               | 2.60 sec: 1.08x faster                                                     |
| unpickle                | 14.1 us                                                | 13.3 us: 1.06x faster                                                      |
| pickle                  | 10.3 us                                                | 10.0 us: 1.03x faster                                                      |
| telco                   | 6.54 ms                                                | 6.44 ms: 1.02x faster                                                      |
| gc_traversal            | 3.84 ms                                                | 3.81 ms: 1.01x faster                                                      |
| generators              | 76.8 ms                                                | 76.3 ms: 1.01x faster                                                      |
| unpickle_list           | 4.82 us                                                | 4.99 us: 1.04x slower                                                      |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                       |
| regex_effbot            | 3.23 ms                                                | 3.44 ms: 1.07x slower                                                      |
| python_startup_no_site  | 5.82 ms                                                | 6.25 ms: 1.07x slower                                                      |
| pickle_dict             | 27.3 us                                                | 30.6 us: 1.12x slower                                                      |
| dask                    | 423 ms                                                 | 514 ms: 1.22x slower                                                       |
| coverage                | 72.8 ms                                                | 102 ms: 1.40x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                               |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230118-3.12.0a4+-34ba834/bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.26x
