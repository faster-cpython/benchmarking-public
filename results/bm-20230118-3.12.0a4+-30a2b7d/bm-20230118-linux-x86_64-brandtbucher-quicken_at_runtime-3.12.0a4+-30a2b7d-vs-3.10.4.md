
# Results vs. 3.10.4

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 30a2b7d
- commit date: 2023-01-18
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 250 ms: 1.34x faster                                                       |
| chameleon      | 9.17 ms                                                | 6.51 ms: 1.41x faster                                                      |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                     |
| html5lib       | 85.9 ms                                                | 60.5 ms: 1.42x faster                                                      |
| tornado_http   | 128 ms                                                 | 94.9 ms: 1.35x faster                                                      |
| Geometric mean | (ref)                                                  | 1.36x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 93.5 ms: 1.54x faster                                                      |
| float          | 109 ms                                                 | 71.8 ms: 1.52x faster                                                      |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.31x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.39x faster                                                       |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                      |
| regex_dna      | 214 ms                                                 | 216 ms: 1.01x slower                                                       |
| regex_effbot   | 3.19 ms                                                | 3.68 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 282 us: 1.60x faster                                                       |
| unpickle_pure_python | 302 us                                                 | 199 us: 1.51x faster                                                       |
| json_dumps           | 13.4 ms                                                | 9.43 ms: 1.43x faster                                                      |
| xml_etree_process    | 74.5 ms                                                | 54.2 ms: 1.37x faster                                                      |
| xml_etree_generate   | 93.8 ms                                                | 78.2 ms: 1.20x faster                                                      |
| json_loads           | 28.7 us                                                | 24.4 us: 1.18x faster                                                      |
| pickle_list          | 4.72 us                                                | 4.11 us: 1.15x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 150 ms: 1.09x faster                                                       |
| unpickle             | 14.2 us                                                | 13.2 us: 1.07x faster                                                      |
| xml_etree_iterparse  | 111 ms                                                 | 107 ms: 1.04x faster                                                       |
| unpickle_list        | 4.92 us                                                | 5.01 us: 1.02x slower                                                      |
| pickle_dict          | 27.6 us                                                | 31.2 us: 1.13x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                               |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.71 ms: 1.62x faster                                                      |
| python_startup_no_site | 5.78 ms                                                | 6.25 ms: 1.08x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.22x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.78 ms: 1.50x faster                                                      |
| genshi_text     | 30.6 ms                                                | 20.8 ms: 1.47x faster                                                      |
| django_template | 46.3 ms                                                | 33.0 ms: 1.40x faster                                                      |
| genshi_xml      | 63.7 ms                                                | 47.1 ms: 1.35x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.17 ms: 2.29x faster                                                      |
| logging_silent          | 176 ns                                                 | 90.1 ns: 1.96x faster                                                      |
| asyncio_tcp             | 914 ms                                                 | 495 ms: 1.85x faster                                                       |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.83x faster                                                       |
| richards                | 75.2 ms                                                | 43.7 ms: 1.72x faster                                                      |
| pyflate                 | 676 ms                                                 | 396 ms: 1.71x faster                                                       |
| go                      | 226 ms                                                 | 133 ms: 1.70x faster                                                       |
| chaos                   | 106 ms                                                 | 62.8 ms: 1.68x faster                                                      |
| raytrace                | 467 ms                                                 | 279 ms: 1.67x faster                                                       |
| scimark_monte_carlo     | 109 ms                                                 | 65.5 ms: 1.66x faster                                                      |
| python_startup          | 14.1 ms                                                | 8.71 ms: 1.62x faster                                                      |
| hexiom                  | 9.43 ms                                                | 5.87 ms: 1.61x faster                                                      |
| pickle_pure_python      | 452 us                                                 | 282 us: 1.60x faster                                                       |
| crypto_pyaes            | 117 ms                                                 | 73.3 ms: 1.59x faster                                                      |
| nbody                   | 144 ms                                                 | 93.5 ms: 1.54x faster                                                      |
| deepcopy_memo           | 51.7 us                                                | 33.8 us: 1.53x faster                                                      |
| float                   | 109 ms                                                 | 71.8 ms: 1.52x faster                                                      |
| unpickle_pure_python    | 302 us                                                 | 199 us: 1.51x faster                                                       |
| scimark_lu              | 161 ms                                                 | 107 ms: 1.51x faster                                                       |
| spectral_norm           | 150 ms                                                 | 99.4 ms: 1.51x faster                                                      |
| mako                    | 14.7 ms                                                | 9.78 ms: 1.50x faster                                                      |
| genshi_text             | 30.6 ms                                                | 20.8 ms: 1.47x faster                                                      |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.46x faster                                                      |
| sqlglot_transpile       | 2.43 ms                                                | 1.69 ms: 1.44x faster                                                      |
| pprint_pformat          | 1.98 sec                                               | 1.38 sec: 1.43x faster                                                     |
| json_dumps              | 13.4 ms                                                | 9.43 ms: 1.43x faster                                                      |
| html5lib                | 85.9 ms                                                | 60.5 ms: 1.42x faster                                                      |
| pprint_safe_repr        | 953 ms                                                 | 676 ms: 1.41x faster                                                       |
| chameleon               | 9.17 ms                                                | 6.51 ms: 1.41x faster                                                      |
| django_template         | 46.3 ms                                                | 33.0 ms: 1.40x faster                                                      |
| logging_simple          | 8.10 us                                                | 5.80 us: 1.40x faster                                                      |
| regex_compile           | 177 ms                                                 | 127 ms: 1.39x faster                                                       |
| scimark_fft             | 421 ms                                                 | 304 ms: 1.39x faster                                                       |
| logging_format          | 8.85 us                                                | 6.40 us: 1.38x faster                                                      |
| thrift                  | 1.03 ms                                                | 752 us: 1.37x faster                                                       |
| xml_etree_process       | 74.5 ms                                                | 54.2 ms: 1.37x faster                                                      |
| fannkuch                | 488 ms                                                 | 357 ms: 1.36x faster                                                       |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.02 ms: 1.36x faster                                                      |
| async_tree_none         | 711 ms                                                 | 525 ms: 1.35x faster                                                       |
| genshi_xml              | 63.7 ms                                                | 47.1 ms: 1.35x faster                                                      |
| tornado_http            | 128 ms                                                 | 94.9 ms: 1.35x faster                                                      |
| aiohttp                 | 1.34 ms                                                | 993 us: 1.35x faster                                                       |
| deepcopy                | 438 us                                                 | 324 us: 1.35x faster                                                       |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                                     |
| 2to3                    | 335 ms                                                 | 250 ms: 1.34x faster                                                       |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                                      |
| pycparser               | 1.53 sec                                               | 1.15 sec: 1.33x faster                                                     |
| async_tree_memoization  | 855 ms                                                 | 642 ms: 1.33x faster                                                       |
| unpack_sequence         | 59.4 ns                                                | 45.1 ns: 1.32x faster                                                      |
| nqueens                 | 100 ms                                                 | 76.9 ms: 1.30x faster                                                      |
| deepcopy_reduce         | 3.79 us                                                | 2.94 us: 1.29x faster                                                      |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.29x faster                                                       |
| sqlglot_optimize        | 65.2 ms                                                | 50.8 ms: 1.28x faster                                                      |
| coroutines              | 31.6 ms                                                | 24.8 ms: 1.27x faster                                                      |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                     |
| async_tree_cpu_io_mixed | 949 ms                                                 | 754 ms: 1.26x faster                                                       |
| sympy_integrate         | 24.0 ms                                                | 19.6 ms: 1.22x faster                                                      |
| async_generators        | 426 ms                                                 | 350 ms: 1.22x faster                                                       |
| bench_thread_pool       | 946 us                                                 | 780 us: 1.21x faster                                                       |
| sympy_str               | 325 ms                                                 | 269 ms: 1.21x faster                                                       |
| dulwich_log             | 75.8 ms                                                | 63.0 ms: 1.20x faster                                                      |
| xml_etree_generate      | 93.8 ms                                                | 78.2 ms: 1.20x faster                                                      |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.18x faster                                                       |
| sympy_expand            | 534 ms                                                 | 452 ms: 1.18x faster                                                       |
| json_loads              | 28.7 us                                                | 24.4 us: 1.18x faster                                                      |
| json                    | 5.35 ms                                                | 4.64 ms: 1.15x faster                                                      |
| pickle_list             | 4.72 us                                                | 4.11 us: 1.15x faster                                                      |
| djangocms               | 36.9 us                                                | 32.2 us: 1.14x faster                                                      |
| create_gc_cycles        | 1.65 ms                                                | 1.46 ms: 1.13x faster                                                      |
| sqlite_synth            | 2.92 us                                                | 2.58 us: 1.13x faster                                                      |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                      |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                      |
| mdp                     | 2.74 sec                                               | 2.49 sec: 1.10x faster                                                     |
| xml_etree_parse         | 163 ms                                                 | 150 ms: 1.09x faster                                                       |
| unpickle                | 14.2 us                                                | 13.2 us: 1.07x faster                                                      |
| telco                   | 6.73 ms                                                | 6.32 ms: 1.06x faster                                                      |
| xml_etree_iterparse     | 111 ms                                                 | 107 ms: 1.04x faster                                                       |
| meteor_contest          | 114 ms                                                 | 111 ms: 1.03x faster                                                       |
| generators              | 76.4 ms                                                | 75.5 ms: 1.01x faster                                                      |
| regex_dna               | 214 ms                                                 | 216 ms: 1.01x slower                                                       |
| unpickle_list           | 4.92 us                                                | 5.01 us: 1.02x slower                                                      |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                       |
| python_startup_no_site  | 5.78 ms                                                | 6.25 ms: 1.08x slower                                                      |
| pickle_dict             | 27.6 us                                                | 31.2 us: 1.13x slower                                                      |
| gc_traversal            | 3.53 ms                                                | 4.06 ms: 1.15x slower                                                      |
| regex_effbot            | 3.19 ms                                                | 3.68 ms: 1.15x slower                                                      |
| dask                    | 436 ms                                                 | 504 ms: 1.15x slower                                                       |
| coverage                | 74.7 ms                                                | 102 ms: 1.37x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                               |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230118-3.12.0a4+-30a2b7d/bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d.json: mypy
