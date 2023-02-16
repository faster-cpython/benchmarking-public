
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: dec1ab0
- commit date: 2023-02-07
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 254 ms: 1.32x faster                                   |
| chameleon      | 9.17 ms                                                | 6.27 ms: 1.46x faster                                  |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                 |
| html5lib       | 85.9 ms                                                | 60.8 ms: 1.41x faster                                  |
| tornado_http   | 128 ms                                                 | 94.6 ms: 1.36x faster                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 109 ms                                                 | 72.1 ms: 1.51x faster                                  |
| nbody          | 144 ms                                                 | 95.4 ms: 1.51x faster                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                  |
| regex_dna      | 214 ms                                                 | 211 ms: 1.01x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.44 ms: 1.08x slower                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 286 us: 1.58x faster                                   |
| unpickle_pure_python | 302 us                                                 | 197 us: 1.53x faster                                   |
| json_dumps           | 13.4 ms                                                | 9.41 ms: 1.43x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 53.9 ms: 1.38x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 77.3 ms: 1.21x faster                                  |
| json_loads           | 28.7 us                                                | 24.1 us: 1.19x faster                                  |
| pickle_list          | 4.72 us                                                | 4.16 us: 1.13x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                   |
| unpickle             | 14.2 us                                                | 13.0 us: 1.09x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.08x faster                                   |
| pickle               | 10.2 us                                                | 10.1 us: 1.01x faster                                  |
| unpickle_list        | 4.92 us                                                | 5.04 us: 1.02x slower                                  |
| pickle_dict          | 27.6 us                                                | 31.2 us: 1.13x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.97 ms: 1.57x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.49 ms: 1.12x slower                                  |
| Geometric mean         | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.72 ms: 1.51x faster                                  |
| genshi_text     | 30.6 ms                                                | 20.4 ms: 1.50x faster                                  |
| django_template | 46.3 ms                                                | 33.5 ms: 1.38x faster                                  |
| genshi_xml      | 63.7 ms                                                | 46.7 ms: 1.37x faster                                  |
| Geometric mean  | (ref)                                                  | 1.44x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.30 ms: 2.21x faster                                  |
| logging_silent          | 176 ns                                                 | 93.8 ns: 1.88x faster                                  |
| asyncio_tcp             | 914 ms                                                 | 494 ms: 1.85x faster                                   |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                   |
| richards                | 75.2 ms                                                | 41.8 ms: 1.80x faster                                  |
| pyflate                 | 676 ms                                                 | 399 ms: 1.69x faster                                   |
| go                      | 226 ms                                                 | 138 ms: 1.64x faster                                   |
| raytrace                | 467 ms                                                 | 287 ms: 1.63x faster                                   |
| chaos                   | 106 ms                                                 | 65.5 ms: 1.61x faster                                  |
| scimark_monte_carlo     | 109 ms                                                 | 68.1 ms: 1.59x faster                                  |
| pickle_pure_python      | 452 us                                                 | 286 us: 1.58x faster                                   |
| hexiom                  | 9.43 ms                                                | 5.99 ms: 1.57x faster                                  |
| python_startup          | 14.1 ms                                                | 8.97 ms: 1.57x faster                                  |
| crypto_pyaes            | 117 ms                                                 | 74.4 ms: 1.57x faster                                  |
| spectral_norm           | 150 ms                                                 | 96.5 ms: 1.55x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 197 us: 1.53x faster                                   |
| float                   | 109 ms                                                 | 72.1 ms: 1.51x faster                                  |
| deepcopy_memo           | 51.7 us                                                | 34.2 us: 1.51x faster                                  |
| nbody                   | 144 ms                                                 | 95.4 ms: 1.51x faster                                  |
| mako                    | 14.7 ms                                                | 9.72 ms: 1.51x faster                                  |
| genshi_text             | 30.6 ms                                                | 20.4 ms: 1.50x faster                                  |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.49x faster                                   |
| chameleon               | 9.17 ms                                                | 6.27 ms: 1.46x faster                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.42 ms: 1.44x faster                                  |
| json_dumps              | 13.4 ms                                                | 9.41 ms: 1.43x faster                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.71 ms: 1.42x faster                                  |
| html5lib                | 85.9 ms                                                | 60.8 ms: 1.41x faster                                  |
| pprint_pformat          | 1.98 sec                                               | 1.42 sec: 1.40x faster                                 |
| logging_simple          | 8.10 us                                                | 5.78 us: 1.40x faster                                  |
| logging_format          | 8.85 us                                                | 6.39 us: 1.38x faster                                  |
| xml_etree_process       | 74.5 ms                                                | 53.9 ms: 1.38x faster                                  |
| django_template         | 46.3 ms                                                | 33.5 ms: 1.38x faster                                  |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                   |
| pprint_safe_repr        | 953 ms                                                 | 695 ms: 1.37x faster                                   |
| scimark_fft             | 421 ms                                                 | 308 ms: 1.37x faster                                   |
| genshi_xml              | 63.7 ms                                                | 46.7 ms: 1.37x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.01 ms: 1.36x faster                                  |
| tornado_http            | 128 ms                                                 | 94.6 ms: 1.36x faster                                  |
| async_tree_none         | 711 ms                                                 | 526 ms: 1.35x faster                                   |
| fannkuch                | 488 ms                                                 | 362 ms: 1.35x faster                                   |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                 |
| deepcopy                | 438 us                                                 | 327 us: 1.34x faster                                   |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.34x faster                                  |
| thrift                  | 1.03 ms                                                | 777 us: 1.33x faster                                   |
| unpack_sequence         | 59.4 ns                                                | 44.7 ns: 1.33x faster                                  |
| pycparser               | 1.53 sec                                               | 1.15 sec: 1.33x faster                                 |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.32x faster                                  |
| 2to3                    | 335 ms                                                 | 254 ms: 1.32x faster                                   |
| mypy2                   | 430 ms                                                 | 331 ms: 1.30x faster                                   |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.29x faster                                   |
| async_tree_memoization  | 855 ms                                                 | 665 ms: 1.29x faster                                   |
| sqlglot_optimize        | 65.2 ms                                                | 50.8 ms: 1.28x faster                                  |
| deepcopy_reduce         | 3.79 us                                                | 2.97 us: 1.28x faster                                  |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                 |
| nqueens                 | 100 ms                                                 | 78.8 ms: 1.27x faster                                  |
| coroutines              | 31.6 ms                                                | 25.2 ms: 1.26x faster                                  |
| async_tree_cpu_io_mixed | 949 ms                                                 | 760 ms: 1.25x faster                                   |
| sympy_integrate         | 24.0 ms                                                | 19.7 ms: 1.22x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 77.3 ms: 1.21x faster                                  |
| bench_thread_pool       | 946 us                                                 | 781 us: 1.21x faster                                   |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.20x faster                                   |
| sympy_str               | 325 ms                                                 | 270 ms: 1.20x faster                                   |
| dulwich_log             | 75.8 ms                                                | 63.1 ms: 1.20x faster                                  |
| async_generators        | 426 ms                                                 | 356 ms: 1.20x faster                                   |
| json_loads              | 28.7 us                                                | 24.1 us: 1.19x faster                                  |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.1 ms: 1.19x faster                                  |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                   |
| sympy_expand            | 534 ms                                                 | 457 ms: 1.17x faster                                   |
| json                    | 5.35 ms                                                | 4.62 ms: 1.16x faster                                  |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.14x faster                                  |
| djangocms               | 36.9 us                                                | 32.3 us: 1.14x faster                                  |
| pickle_list             | 4.72 us                                                | 4.16 us: 1.13x faster                                  |
| sqlite_synth            | 2.92 us                                                | 2.58 us: 1.13x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                  |
| create_gc_cycles        | 1.65 ms                                                | 1.47 ms: 1.12x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                   |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                   |
| unpickle                | 14.2 us                                                | 13.0 us: 1.09x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.08x faster                                   |
| telco                   | 6.73 ms                                                | 6.38 ms: 1.06x faster                                  |
| regex_dna               | 214 ms                                                 | 211 ms: 1.01x faster                                   |
| pickle                  | 10.2 us                                                | 10.1 us: 1.01x faster                                  |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| generators              | 76.4 ms                                                | 76.8 ms: 1.00x slower                                  |
| unpickle_list           | 4.92 us                                                | 5.04 us: 1.02x slower                                  |
| gc_traversal            | 3.53 ms                                                | 3.80 ms: 1.08x slower                                  |
| regex_effbot            | 3.19 ms                                                | 3.44 ms: 1.08x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.49 ms: 1.12x slower                                  |
| pickle_dict             | 27.6 us                                                | 31.2 us: 1.13x slower                                  |
| dask                    | 436 ms                                                 | 504 ms: 1.15x slower                                   |
| coverage                | 74.7 ms                                                | 95.3 ms: 1.28x slower                                  |
| Geometric mean          | (ref)                                                  | 1.29x faster                                           |

Benchmark hidden because not significant (2): mdp, bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
