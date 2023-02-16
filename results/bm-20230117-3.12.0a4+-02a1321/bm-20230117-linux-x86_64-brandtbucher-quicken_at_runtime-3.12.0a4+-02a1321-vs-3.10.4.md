
# Results vs. 3.10.4

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 02a1321
- commit date: 2023-01-17
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 256 ms: 1.31x faster                                                       |
| chameleon      | 9.17 ms                                                | 6.32 ms: 1.45x faster                                                      |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.27x faster                                                     |
| html5lib       | 85.9 ms                                                | 61.5 ms: 1.40x faster                                                      |
| tornado_http   | 128 ms                                                 | 94.4 ms: 1.36x faster                                                      |
| Geometric mean | (ref)                                                  | 1.35x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.0 ms: 1.53x faster                                                      |
| float          | 109 ms                                                 | 76.0 ms: 1.43x faster                                                      |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                  | 1.29x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 130 ms: 1.37x faster                                                       |
| regex_v8       | 25.0 ms                                                | 21.5 ms: 1.16x faster                                                      |
| regex_dna      | 214 ms                                                 | 209 ms: 1.03x faster                                                       |
| regex_effbot   | 3.19 ms                                                | 3.65 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                  | 1.09x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 293 us: 1.54x faster                                                       |
| unpickle_pure_python | 302 us                                                 | 209 us: 1.45x faster                                                       |
| json_dumps           | 13.4 ms                                                | 9.34 ms: 1.44x faster                                                      |
| xml_etree_process    | 74.5 ms                                                | 53.2 ms: 1.40x faster                                                      |
| xml_etree_generate   | 93.8 ms                                                | 76.9 ms: 1.22x faster                                                      |
| json_loads           | 28.7 us                                                | 23.9 us: 1.20x faster                                                      |
| pickle_list          | 4.72 us                                                | 4.08 us: 1.16x faster                                                      |
| unpickle             | 14.2 us                                                | 13.0 us: 1.09x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 151 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                 | 105 ms: 1.06x faster                                                       |
| pickle               | 10.2 us                                                | 10.1 us: 1.01x faster                                                      |
| pickle_dict          | 27.6 us                                                | 30.8 us: 1.12x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.74 ms: 1.61x faster                                                      |
| python_startup_no_site | 5.78 ms                                                | 6.27 ms: 1.08x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.22x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.2 ms: 1.52x faster                                                      |
| mako            | 14.7 ms                                                | 9.71 ms: 1.51x faster                                                      |
| django_template | 46.3 ms                                                | 32.6 ms: 1.42x faster                                                      |
| genshi_xml      | 63.7 ms                                                | 46.2 ms: 1.38x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.50 ms: 2.08x faster                                                      |
| logging_silent          | 176 ns                                                 | 89.6 ns: 1.97x faster                                                      |
| asyncio_tcp             | 914 ms                                                 | 494 ms: 1.85x faster                                                       |
| scimark_sor             | 197 ms                                                 | 119 ms: 1.65x faster                                                       |
| chaos                   | 106 ms                                                 | 64.7 ms: 1.63x faster                                                      |
| go                      | 226 ms                                                 | 139 ms: 1.63x faster                                                       |
| crypto_pyaes            | 117 ms                                                 | 72.0 ms: 1.62x faster                                                      |
| richards                | 75.2 ms                                                | 46.6 ms: 1.61x faster                                                      |
| python_startup          | 14.1 ms                                                | 8.74 ms: 1.61x faster                                                      |
| pyflate                 | 676 ms                                                 | 420 ms: 1.61x faster                                                       |
| hexiom                  | 9.43 ms                                                | 6.00 ms: 1.57x faster                                                      |
| raytrace                | 467 ms                                                 | 299 ms: 1.56x faster                                                       |
| scimark_monte_carlo     | 109 ms                                                 | 69.8 ms: 1.55x faster                                                      |
| pickle_pure_python      | 452 us                                                 | 293 us: 1.54x faster                                                       |
| spectral_norm           | 150 ms                                                 | 97.5 ms: 1.53x faster                                                      |
| nbody                   | 144 ms                                                 | 94.0 ms: 1.53x faster                                                      |
| genshi_text             | 30.6 ms                                                | 20.2 ms: 1.52x faster                                                      |
| deepcopy_memo           | 51.7 us                                                | 34.1 us: 1.52x faster                                                      |
| scimark_lu              | 161 ms                                                 | 107 ms: 1.51x faster                                                       |
| mako                    | 14.7 ms                                                | 9.71 ms: 1.51x faster                                                      |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.45x faster                                                      |
| chameleon               | 9.17 ms                                                | 6.32 ms: 1.45x faster                                                      |
| unpickle_pure_python    | 302 us                                                 | 209 us: 1.45x faster                                                       |
| pprint_pformat          | 1.98 sec                                               | 1.38 sec: 1.44x faster                                                     |
| json_dumps              | 13.4 ms                                                | 9.34 ms: 1.44x faster                                                      |
| float                   | 109 ms                                                 | 76.0 ms: 1.43x faster                                                      |
| pprint_safe_repr        | 953 ms                                                 | 670 ms: 1.42x faster                                                       |
| django_template         | 46.3 ms                                                | 32.6 ms: 1.42x faster                                                      |
| sqlglot_transpile       | 2.43 ms                                                | 1.71 ms: 1.42x faster                                                      |
| xml_etree_process       | 74.5 ms                                                | 53.2 ms: 1.40x faster                                                      |
| thrift                  | 1.03 ms                                                | 738 us: 1.40x faster                                                       |
| html5lib                | 85.9 ms                                                | 61.5 ms: 1.40x faster                                                      |
| logging_simple          | 8.10 us                                                | 5.81 us: 1.40x faster                                                      |
| genshi_xml              | 63.7 ms                                                | 46.2 ms: 1.38x faster                                                      |
| pycparser               | 1.53 sec                                               | 1.11 sec: 1.37x faster                                                     |
| logging_format          | 8.85 us                                                | 6.45 us: 1.37x faster                                                      |
| regex_compile           | 177 ms                                                 | 130 ms: 1.37x faster                                                       |
| unpack_sequence         | 59.4 ns                                                | 43.5 ns: 1.37x faster                                                      |
| async_tree_none         | 711 ms                                                 | 522 ms: 1.36x faster                                                       |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.36x faster                                                     |
| scimark_fft             | 421 ms                                                 | 310 ms: 1.36x faster                                                       |
| tornado_http            | 128 ms                                                 | 94.4 ms: 1.36x faster                                                      |
| deepcopy                | 438 us                                                 | 326 us: 1.34x faster                                                       |
| aiohttp                 | 1.34 ms                                                | 998 us: 1.34x faster                                                       |
| async_tree_memoization  | 855 ms                                                 | 637 ms: 1.34x faster                                                       |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.33x faster                                                      |
| 2to3                    | 335 ms                                                 | 256 ms: 1.31x faster                                                       |
| deepcopy_reduce         | 3.79 us                                                | 2.95 us: 1.28x faster                                                      |
| nqueens                 | 100 ms                                                 | 78.0 ms: 1.28x faster                                                      |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.26 ms: 1.28x faster                                                      |
| sqlglot_optimize        | 65.2 ms                                                | 51.1 ms: 1.28x faster                                                      |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                       |
| fannkuch                | 488 ms                                                 | 385 ms: 1.27x faster                                                       |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.27x faster                                                     |
| async_tree_cpu_io_mixed | 949 ms                                                 | 763 ms: 1.24x faster                                                       |
| coroutines              | 31.6 ms                                                | 25.6 ms: 1.24x faster                                                      |
| xml_etree_generate      | 93.8 ms                                                | 76.9 ms: 1.22x faster                                                      |
| async_generators        | 426 ms                                                 | 350 ms: 1.22x faster                                                       |
| dulwich_log             | 75.8 ms                                                | 62.4 ms: 1.22x faster                                                      |
| bench_thread_pool       | 946 us                                                 | 782 us: 1.21x faster                                                       |
| sympy_integrate         | 24.0 ms                                                | 20.0 ms: 1.20x faster                                                      |
| json_loads              | 28.7 us                                                | 23.9 us: 1.20x faster                                                      |
| sympy_str               | 325 ms                                                 | 271 ms: 1.20x faster                                                       |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.18x faster                                                       |
| json                    | 5.35 ms                                                | 4.56 ms: 1.17x faster                                                      |
| sympy_expand            | 534 ms                                                 | 455 ms: 1.17x faster                                                       |
| regex_v8                | 25.0 ms                                                | 21.5 ms: 1.16x faster                                                      |
| pickle_list             | 4.72 us                                                | 4.08 us: 1.16x faster                                                      |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                      |
| sqlite_synth            | 2.92 us                                                | 2.59 us: 1.13x faster                                                      |
| djangocms               | 36.9 us                                                | 32.8 us: 1.12x faster                                                      |
| create_gc_cycles        | 1.65 ms                                                | 1.48 ms: 1.12x faster                                                      |
| unpickle                | 14.2 us                                                | 13.0 us: 1.09x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 151 ms: 1.08x faster                                                       |
| meteor_contest          | 114 ms                                                 | 106 ms: 1.07x faster                                                       |
| telco                   | 6.73 ms                                                | 6.34 ms: 1.06x faster                                                      |
| xml_etree_iterparse     | 111 ms                                                 | 105 ms: 1.06x faster                                                       |
| mdp                     | 2.74 sec                                               | 2.61 sec: 1.05x faster                                                     |
| regex_dna               | 214 ms                                                 | 209 ms: 1.03x faster                                                       |
| generators              | 76.4 ms                                                | 75.2 ms: 1.02x faster                                                      |
| pickle                  | 10.2 us                                                | 10.1 us: 1.01x faster                                                      |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                                       |
| gc_traversal            | 3.53 ms                                                | 3.59 ms: 1.02x slower                                                      |
| python_startup_no_site  | 5.78 ms                                                | 6.27 ms: 1.08x slower                                                      |
| pickle_dict             | 27.6 us                                                | 30.8 us: 1.12x slower                                                      |
| regex_effbot            | 3.19 ms                                                | 3.65 ms: 1.14x slower                                                      |
| dask                    | 436 ms                                                 | 512 ms: 1.17x slower                                                       |
| coverage                | 74.7 ms                                                | 96.7 ms: 1.29x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                               |

Benchmark hidden because not significant (2): bench_mp_pool, unpickle_list
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230117-3.12.0a4+-02a1321/bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321.json: mypy
