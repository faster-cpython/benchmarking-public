
# Results vs. 3.10.4

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 34ba834
- commit date: 2023-01-18
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 256 ms: 1.31x faster                                                       |
| chameleon      | 9.17 ms                                                | 6.56 ms: 1.40x faster                                                      |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                     |
| html5lib       | 85.9 ms                                                | 61.4 ms: 1.40x faster                                                      |
| tornado_http   | 128 ms                                                 | 94.7 ms: 1.35x faster                                                      |
| Geometric mean | (ref)                                                  | 1.35x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 92.5 ms: 1.56x faster                                                      |
| float          | 109 ms                                                 | 74.3 ms: 1.47x faster                                                      |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.30x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 130 ms: 1.36x faster                                                       |
| regex_v8       | 25.0 ms                                                | 21.1 ms: 1.19x faster                                                      |
| regex_dna      | 214 ms                                                 | 201 ms: 1.06x faster                                                       |
| regex_effbot   | 3.19 ms                                                | 3.44 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                  | 1.12x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 290 us: 1.56x faster                                                       |
| unpickle_pure_python | 302 us                                                 | 209 us: 1.44x faster                                                       |
| json_dumps           | 13.4 ms                                                | 9.55 ms: 1.41x faster                                                      |
| xml_etree_process    | 74.5 ms                                                | 53.5 ms: 1.39x faster                                                      |
| xml_etree_generate   | 93.8 ms                                                | 77.2 ms: 1.22x faster                                                      |
| json_loads           | 28.7 us                                                | 24.4 us: 1.18x faster                                                      |
| pickle_list          | 4.72 us                                                | 4.02 us: 1.17x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                       |
| unpickle             | 14.2 us                                                | 13.3 us: 1.06x faster                                                      |
| pickle               | 10.2 us                                                | 10.0 us: 1.01x faster                                                      |
| unpickle_list        | 4.92 us                                                | 4.99 us: 1.01x slower                                                      |
| pickle_dict          | 27.6 us                                                | 30.6 us: 1.11x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.72 ms: 1.62x faster                                                      |
| python_startup_no_site | 5.78 ms                                                | 6.25 ms: 1.08x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.22x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.57 ms: 1.53x faster                                                      |
| genshi_text     | 30.6 ms                                                | 20.5 ms: 1.49x faster                                                      |
| django_template | 46.3 ms                                                | 32.7 ms: 1.42x faster                                                      |
| genshi_xml      | 63.7 ms                                                | 48.1 ms: 1.32x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.32 ms: 2.19x faster                                                      |
| logging_silent          | 176 ns                                                 | 92.3 ns: 1.91x faster                                                      |
| asyncio_tcp             | 914 ms                                                 | 491 ms: 1.86x faster                                                       |
| richards                | 75.2 ms                                                | 43.8 ms: 1.72x faster                                                      |
| raytrace                | 467 ms                                                 | 282 ms: 1.66x faster                                                       |
| go                      | 226 ms                                                 | 139 ms: 1.62x faster                                                       |
| scimark_sor             | 197 ms                                                 | 121 ms: 1.62x faster                                                       |
| chaos                   | 106 ms                                                 | 65.3 ms: 1.62x faster                                                      |
| python_startup          | 14.1 ms                                                | 8.72 ms: 1.62x faster                                                      |
| scimark_monte_carlo     | 109 ms                                                 | 67.6 ms: 1.61x faster                                                      |
| pyflate                 | 676 ms                                                 | 421 ms: 1.61x faster                                                       |
| crypto_pyaes            | 117 ms                                                 | 72.8 ms: 1.60x faster                                                      |
| spectral_norm           | 150 ms                                                 | 95.4 ms: 1.57x faster                                                      |
| pickle_pure_python      | 452 us                                                 | 290 us: 1.56x faster                                                       |
| nbody                   | 144 ms                                                 | 92.5 ms: 1.56x faster                                                      |
| hexiom                  | 9.43 ms                                                | 6.12 ms: 1.54x faster                                                      |
| mako                    | 14.7 ms                                                | 9.57 ms: 1.53x faster                                                      |
| deepcopy_memo           | 51.7 us                                                | 34.0 us: 1.52x faster                                                      |
| scimark_lu              | 161 ms                                                 | 107 ms: 1.50x faster                                                       |
| genshi_text             | 30.6 ms                                                | 20.5 ms: 1.49x faster                                                      |
| float                   | 109 ms                                                 | 74.3 ms: 1.47x faster                                                      |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.45x faster                                                      |
| unpickle_pure_python    | 302 us                                                 | 209 us: 1.44x faster                                                       |
| pprint_pformat          | 1.98 sec                                               | 1.38 sec: 1.44x faster                                                     |
| sqlglot_transpile       | 2.43 ms                                                | 1.70 ms: 1.43x faster                                                      |
| django_template         | 46.3 ms                                                | 32.7 ms: 1.42x faster                                                      |
| pprint_safe_repr        | 953 ms                                                 | 677 ms: 1.41x faster                                                       |
| json_dumps              | 13.4 ms                                                | 9.55 ms: 1.41x faster                                                      |
| html5lib                | 85.9 ms                                                | 61.4 ms: 1.40x faster                                                      |
| chameleon               | 9.17 ms                                                | 6.56 ms: 1.40x faster                                                      |
| thrift                  | 1.03 ms                                                | 741 us: 1.40x faster                                                       |
| xml_etree_process       | 74.5 ms                                                | 53.5 ms: 1.39x faster                                                      |
| logging_simple          | 8.10 us                                                | 5.85 us: 1.38x faster                                                      |
| pycparser               | 1.53 sec                                               | 1.11 sec: 1.38x faster                                                     |
| scimark_fft             | 421 ms                                                 | 305 ms: 1.38x faster                                                       |
| logging_format          | 8.85 us                                                | 6.42 us: 1.38x faster                                                      |
| unpack_sequence         | 59.4 ns                                                | 43.3 ns: 1.37x faster                                                      |
| regex_compile           | 177 ms                                                 | 130 ms: 1.36x faster                                                       |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.36x faster                                                     |
| tornado_http            | 128 ms                                                 | 94.7 ms: 1.35x faster                                                      |
| async_tree_none         | 711 ms                                                 | 526 ms: 1.35x faster                                                       |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.34x faster                                                      |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.33x faster                                                      |
| deepcopy                | 438 us                                                 | 329 us: 1.33x faster                                                       |
| genshi_xml              | 63.7 ms                                                | 48.1 ms: 1.32x faster                                                      |
| 2to3                    | 335 ms                                                 | 256 ms: 1.31x faster                                                       |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.16 ms: 1.31x faster                                                      |
| async_tree_memoization  | 855 ms                                                 | 659 ms: 1.30x faster                                                       |
| fannkuch                | 488 ms                                                 | 378 ms: 1.29x faster                                                       |
| sqlglot_optimize        | 65.2 ms                                                | 50.8 ms: 1.28x faster                                                      |
| deepcopy_reduce         | 3.79 us                                                | 2.96 us: 1.28x faster                                                      |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                       |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                     |
| nqueens                 | 100 ms                                                 | 78.7 ms: 1.27x faster                                                      |
| async_tree_cpu_io_mixed | 949 ms                                                 | 756 ms: 1.25x faster                                                       |
| coroutines              | 31.6 ms                                                | 25.8 ms: 1.23x faster                                                      |
| xml_etree_generate      | 93.8 ms                                                | 77.2 ms: 1.22x faster                                                      |
| dulwich_log             | 75.8 ms                                                | 62.9 ms: 1.21x faster                                                      |
| sympy_integrate         | 24.0 ms                                                | 20.0 ms: 1.20x faster                                                      |
| sympy_str               | 325 ms                                                 | 271 ms: 1.20x faster                                                       |
| bench_thread_pool       | 946 us                                                 | 791 us: 1.20x faster                                                       |
| regex_v8                | 25.0 ms                                                | 21.1 ms: 1.19x faster                                                      |
| async_generators        | 426 ms                                                 | 359 ms: 1.19x faster                                                       |
| json_loads              | 28.7 us                                                | 24.4 us: 1.18x faster                                                      |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                                       |
| pickle_list             | 4.72 us                                                | 4.02 us: 1.17x faster                                                      |
| sympy_expand            | 534 ms                                                 | 455 ms: 1.17x faster                                                       |
| json                    | 5.35 ms                                                | 4.67 ms: 1.14x faster                                                      |
| djangocms               | 36.9 us                                                | 32.4 us: 1.14x faster                                                      |
| create_gc_cycles        | 1.65 ms                                                | 1.45 ms: 1.14x faster                                                      |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                      |
| sqlite_synth            | 2.92 us                                                | 2.61 us: 1.12x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                       |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                       |
| meteor_contest          | 114 ms                                                 | 106 ms: 1.08x faster                                                       |
| regex_dna               | 214 ms                                                 | 201 ms: 1.06x faster                                                       |
| unpickle                | 14.2 us                                                | 13.3 us: 1.06x faster                                                      |
| mdp                     | 2.74 sec                                               | 2.60 sec: 1.05x faster                                                     |
| telco                   | 6.73 ms                                                | 6.44 ms: 1.05x faster                                                      |
| pickle                  | 10.2 us                                                | 10.0 us: 1.01x faster                                                      |
| unpickle_list           | 4.92 us                                                | 4.99 us: 1.01x slower                                                      |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                       |
| regex_effbot            | 3.19 ms                                                | 3.44 ms: 1.08x slower                                                      |
| gc_traversal            | 3.53 ms                                                | 3.81 ms: 1.08x slower                                                      |
| python_startup_no_site  | 5.78 ms                                                | 6.25 ms: 1.08x slower                                                      |
| pickle_dict             | 27.6 us                                                | 30.6 us: 1.11x slower                                                      |
| dask                    | 436 ms                                                 | 514 ms: 1.18x slower                                                       |
| coverage                | 74.7 ms                                                | 102 ms: 1.36x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                               |

Benchmark hidden because not significant (2): generators, bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230118-3.12.0a4+-34ba834/bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834.json: mypy
