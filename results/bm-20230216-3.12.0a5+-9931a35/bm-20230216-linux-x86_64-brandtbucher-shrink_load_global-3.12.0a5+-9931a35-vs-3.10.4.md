
# Results vs. 3.10.4

- fork: brandtbucher
- ref: shrink_load_global
- machine: linux-x86_64
- commit hash: 9931a35
- commit date: 2023-02-16
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230216-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-9931a35 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 246 ms: 1.36x faster                                                       |
| chameleon      | 9.17 ms                                                | 6.52 ms: 1.41x faster                                                      |
| docutils       | 3.18 sec                                               | 2.54 sec: 1.25x faster                                                     |
| html5lib       | 85.9 ms                                                | 60.9 ms: 1.41x faster                                                      |
| tornado_http   | 128 ms                                                 | 95.2 ms: 1.35x faster                                                      |
| Geometric mean | (ref)                                                  | 1.35x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230216-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-9931a35 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.4 ms: 1.52x faster                                                      |
| float          | 109 ms                                                 | 72.9 ms: 1.49x faster                                                      |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.32x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230216-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-9931a35 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                                       |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                      |
| regex_dna      | 214 ms                                                 | 206 ms: 1.04x faster                                                       |
| regex_effbot   | 3.19 ms                                                | 3.70 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                  | 1.09x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230216-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-9931a35 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 283 us: 1.60x faster                                                       |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.53x faster                                                       |
| json_dumps           | 13.4 ms                                                | 9.64 ms: 1.40x faster                                                      |
| xml_etree_process    | 74.5 ms                                                | 56.3 ms: 1.32x faster                                                      |
| json_loads           | 28.7 us                                                | 24.2 us: 1.18x faster                                                      |
| xml_etree_generate   | 93.8 ms                                                | 81.9 ms: 1.15x faster                                                      |
| pickle_list          | 4.72 us                                                | 4.26 us: 1.11x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.08x faster                                                       |
| unpickle             | 14.2 us                                                | 13.6 us: 1.04x faster                                                      |
| unpickle_list        | 4.92 us                                                | 5.06 us: 1.03x slower                                                      |
| pickle_dict          | 27.6 us                                                | 31.7 us: 1.15x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                               |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230216-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-9931a35 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.96 ms: 1.57x faster                                                      |
| python_startup_no_site | 5.78 ms                                                | 6.49 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230216-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-9931a35 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 10.0 ms: 1.46x faster                                                      |
| genshi_text     | 30.6 ms                                                | 21.3 ms: 1.44x faster                                                      |
| django_template | 46.3 ms                                                | 33.1 ms: 1.40x faster                                                      |
| genshi_xml      | 63.7 ms                                                | 48.4 ms: 1.32x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230216-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-9931a35 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 30.6 ms: 2.50x faster                                                      |
| deltablue               | 7.28 ms                                                | 3.20 ms: 2.28x faster                                                      |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                                       |
| logging_silent          | 176 ns                                                 | 95.8 ns: 1.84x faster                                                      |
| asyncio_tcp             | 914 ms                                                 | 504 ms: 1.81x faster                                                       |
| richards                | 75.2 ms                                                | 42.2 ms: 1.78x faster                                                      |
| pyflate                 | 676 ms                                                 | 401 ms: 1.68x faster                                                       |
| go                      | 226 ms                                                 | 136 ms: 1.66x faster                                                       |
| scimark_monte_carlo     | 109 ms                                                 | 66.0 ms: 1.64x faster                                                      |
| raytrace                | 467 ms                                                 | 287 ms: 1.63x faster                                                       |
| pickle_pure_python      | 452 us                                                 | 283 us: 1.60x faster                                                       |
| crypto_pyaes            | 117 ms                                                 | 73.6 ms: 1.59x faster                                                      |
| chaos                   | 106 ms                                                 | 66.7 ms: 1.58x faster                                                      |
| spectral_norm           | 150 ms                                                 | 94.9 ms: 1.58x faster                                                      |
| python_startup          | 14.1 ms                                                | 8.96 ms: 1.57x faster                                                      |
| hexiom                  | 9.43 ms                                                | 6.12 ms: 1.54x faster                                                      |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.53x faster                                                       |
| nbody                   | 144 ms                                                 | 94.4 ms: 1.52x faster                                                      |
| float                   | 109 ms                                                 | 72.9 ms: 1.49x faster                                                      |
| deepcopy_memo           | 51.7 us                                                | 34.9 us: 1.48x faster                                                      |
| scimark_lu              | 161 ms                                                 | 109 ms: 1.47x faster                                                       |
| mako                    | 14.7 ms                                                | 10.0 ms: 1.46x faster                                                      |
| genshi_text             | 30.6 ms                                                | 21.3 ms: 1.44x faster                                                      |
| unpack_sequence         | 59.4 ns                                                | 41.8 ns: 1.42x faster                                                      |
| sqlglot_parse           | 2.04 ms                                                | 1.44 ms: 1.42x faster                                                      |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.42x faster                                                     |
| html5lib                | 85.9 ms                                                | 60.9 ms: 1.41x faster                                                      |
| chameleon               | 9.17 ms                                                | 6.52 ms: 1.41x faster                                                      |
| pycparser               | 1.53 sec                                               | 1.09 sec: 1.40x faster                                                     |
| pprint_safe_repr        | 953 ms                                                 | 681 ms: 1.40x faster                                                       |
| coroutines              | 31.6 ms                                                | 22.6 ms: 1.40x faster                                                      |
| sqlglot_transpile       | 2.43 ms                                                | 1.73 ms: 1.40x faster                                                      |
| django_template         | 46.3 ms                                                | 33.1 ms: 1.40x faster                                                      |
| json_dumps              | 13.4 ms                                                | 9.64 ms: 1.40x faster                                                      |
| logging_simple          | 8.10 us                                                | 5.82 us: 1.39x faster                                                      |
| logging_format          | 8.85 us                                                | 6.37 us: 1.39x faster                                                      |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                                       |
| 2to3                    | 335 ms                                                 | 246 ms: 1.36x faster                                                       |
| scimark_fft             | 421 ms                                                 | 309 ms: 1.36x faster                                                       |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.36x faster                                                     |
| async_tree_none         | 711 ms                                                 | 525 ms: 1.35x faster                                                       |
| thrift                  | 1.03 ms                                                | 766 us: 1.35x faster                                                       |
| tornado_http            | 128 ms                                                 | 95.2 ms: 1.35x faster                                                      |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.08 ms: 1.34x faster                                                      |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.34x faster                                                      |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.33x faster                                                      |
| async_tree_memoization  | 855 ms                                                 | 644 ms: 1.33x faster                                                       |
| xml_etree_process       | 74.5 ms                                                | 56.3 ms: 1.32x faster                                                      |
| genshi_xml              | 63.7 ms                                                | 48.4 ms: 1.32x faster                                                      |
| fannkuch                | 488 ms                                                 | 371 ms: 1.31x faster                                                       |
| mypy2                   | 430 ms                                                 | 330 ms: 1.30x faster                                                       |
| deepcopy                | 438 us                                                 | 337 us: 1.30x faster                                                       |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.29x faster                                                       |
| async_tree_cpu_io_mixed | 949 ms                                                 | 743 ms: 1.28x faster                                                       |
| sqlglot_optimize        | 65.2 ms                                                | 51.1 ms: 1.28x faster                                                      |
| deepcopy_reduce         | 3.79 us                                                | 2.98 us: 1.27x faster                                                      |
| docutils                | 3.18 sec                                               | 2.54 sec: 1.25x faster                                                     |
| nqueens                 | 100 ms                                                 | 80.5 ms: 1.24x faster                                                      |
| sympy_integrate         | 24.0 ms                                                | 19.9 ms: 1.21x faster                                                      |
| dulwich_log             | 75.8 ms                                                | 62.9 ms: 1.21x faster                                                      |
| sympy_str               | 325 ms                                                 | 271 ms: 1.20x faster                                                       |
| bench_thread_pool       | 946 us                                                 | 792 us: 1.20x faster                                                       |
| sqlalchemy_declarative  | 165 ms                                                 | 138 ms: 1.19x faster                                                       |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.1 ms: 1.19x faster                                                      |
| json_loads              | 28.7 us                                                | 24.2 us: 1.18x faster                                                      |
| sympy_expand            | 534 ms                                                 | 455 ms: 1.17x faster                                                       |
| sympy_sum               | 183 ms                                                 | 157 ms: 1.16x faster                                                       |
| json                    | 5.35 ms                                                | 4.60 ms: 1.16x faster                                                      |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                      |
| xml_etree_generate      | 93.8 ms                                                | 81.9 ms: 1.15x faster                                                      |
| djangocms               | 36.9 us                                                | 32.9 us: 1.12x faster                                                      |
| create_gc_cycles        | 1.65 ms                                                | 1.47 ms: 1.12x faster                                                      |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                      |
| sqlite_synth            | 2.92 us                                                | 2.63 us: 1.11x faster                                                      |
| pickle_list             | 4.72 us                                                | 4.26 us: 1.11x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                       |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                       |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.08x faster                                                       |
| telco                   | 6.73 ms                                                | 6.38 ms: 1.06x faster                                                      |
| unpickle                | 14.2 us                                                | 13.6 us: 1.04x faster                                                      |
| regex_dna               | 214 ms                                                 | 206 ms: 1.04x faster                                                       |
| async_generators        | 426 ms                                                 | 412 ms: 1.03x faster                                                       |
| mdp                     | 2.74 sec                                               | 2.68 sec: 1.02x faster                                                     |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                       |
| unpickle_list           | 4.92 us                                                | 5.06 us: 1.03x slower                                                      |
| gc_traversal            | 3.53 ms                                                | 3.66 ms: 1.04x slower                                                      |
| python_startup_no_site  | 5.78 ms                                                | 6.49 ms: 1.12x slower                                                      |
| dask                    | 436 ms                                                 | 500 ms: 1.15x slower                                                       |
| pickle_dict             | 27.6 us                                                | 31.7 us: 1.15x slower                                                      |
| regex_effbot            | 3.19 ms                                                | 3.70 ms: 1.16x slower                                                      |
| coverage                | 74.7 ms                                                | 96.8 ms: 1.29x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                               |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
