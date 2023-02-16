
# Results vs. 3.10.4

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: fa5965d
- commit date: 2023-02-02
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 251 ms: 1.34x faster                                                       |
| chameleon      | 9.17 ms                                                | 6.26 ms: 1.46x faster                                                      |
| docutils       | 3.18 sec                                               | 2.49 sec: 1.27x faster                                                     |
| html5lib       | 85.9 ms                                                | 60.1 ms: 1.43x faster                                                      |
| tornado_http   | 128 ms                                                 | 94.3 ms: 1.36x faster                                                      |
| Geometric mean | (ref)                                                  | 1.37x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 109 ms                                                 | 71.9 ms: 1.52x faster                                                      |
| nbody          | 144 ms                                                 | 98.9 ms: 1.46x faster                                                      |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.28x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.39x faster                                                       |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.16x faster                                                      |
| regex_dna      | 214 ms                                                 | 210 ms: 1.02x faster                                                       |
| regex_effbot   | 3.19 ms                                                | 3.40 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                  | 1.11x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 285 us: 1.59x faster                                                       |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.52x faster                                                       |
| json_dumps           | 13.4 ms                                                | 9.40 ms: 1.43x faster                                                      |
| xml_etree_process    | 74.5 ms                                                | 53.1 ms: 1.40x faster                                                      |
| xml_etree_generate   | 93.8 ms                                                | 76.7 ms: 1.22x faster                                                      |
| json_loads           | 28.7 us                                                | 23.9 us: 1.20x faster                                                      |
| pickle_list          | 4.72 us                                                | 4.15 us: 1.14x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                       |
| unpickle             | 14.2 us                                                | 13.1 us: 1.08x faster                                                      |
| pickle               | 10.2 us                                                | 10.3 us: 1.01x slower                                                      |
| unpickle_list        | 4.92 us                                                | 5.07 us: 1.03x slower                                                      |
| pickle_dict          | 27.6 us                                                | 31.0 us: 1.13x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.72 ms: 1.61x faster                                                      |
| python_startup_no_site | 5.78 ms                                                | 6.25 ms: 1.08x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.22x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.53 ms: 1.54x faster                                                      |
| genshi_text     | 30.6 ms                                                | 21.3 ms: 1.44x faster                                                      |
| django_template | 46.3 ms                                                | 32.9 ms: 1.41x faster                                                      |
| genshi_xml      | 63.7 ms                                                | 47.8 ms: 1.33x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.21 ms: 2.27x faster                                                      |
| logging_silent          | 176 ns                                                 | 92.0 ns: 1.92x faster                                                      |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                                       |
| asyncio_tcp             | 914 ms                                                 | 496 ms: 1.84x faster                                                       |
| richards                | 75.2 ms                                                | 42.2 ms: 1.78x faster                                                      |
| pyflate                 | 676 ms                                                 | 394 ms: 1.72x faster                                                       |
| go                      | 226 ms                                                 | 134 ms: 1.68x faster                                                       |
| scimark_monte_carlo     | 109 ms                                                 | 65.2 ms: 1.67x faster                                                      |
| raytrace                | 467 ms                                                 | 282 ms: 1.66x faster                                                       |
| chaos                   | 106 ms                                                 | 64.5 ms: 1.64x faster                                                      |
| python_startup          | 14.1 ms                                                | 8.72 ms: 1.61x faster                                                      |
| crypto_pyaes            | 117 ms                                                 | 73.1 ms: 1.60x faster                                                      |
| hexiom                  | 9.43 ms                                                | 5.93 ms: 1.59x faster                                                      |
| pickle_pure_python      | 452 us                                                 | 285 us: 1.59x faster                                                       |
| spectral_norm           | 150 ms                                                 | 96.8 ms: 1.55x faster                                                      |
| mako                    | 14.7 ms                                                | 9.53 ms: 1.54x faster                                                      |
| scimark_lu              | 161 ms                                                 | 105 ms: 1.53x faster                                                       |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.52x faster                                                       |
| deepcopy_memo           | 51.7 us                                                | 34.0 us: 1.52x faster                                                      |
| float                   | 109 ms                                                 | 71.9 ms: 1.52x faster                                                      |
| chameleon               | 9.17 ms                                                | 6.26 ms: 1.46x faster                                                      |
| nbody                   | 144 ms                                                 | 98.9 ms: 1.46x faster                                                      |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.45x faster                                                      |
| genshi_text             | 30.6 ms                                                | 21.3 ms: 1.44x faster                                                      |
| sqlglot_transpile       | 2.43 ms                                                | 1.69 ms: 1.43x faster                                                      |
| json_dumps              | 13.4 ms                                                | 9.40 ms: 1.43x faster                                                      |
| html5lib                | 85.9 ms                                                | 60.1 ms: 1.43x faster                                                      |
| pprint_pformat          | 1.98 sec                                               | 1.39 sec: 1.42x faster                                                     |
| pprint_safe_repr        | 953 ms                                                 | 676 ms: 1.41x faster                                                       |
| django_template         | 46.3 ms                                                | 32.9 ms: 1.41x faster                                                      |
| xml_etree_process       | 74.5 ms                                                | 53.1 ms: 1.40x faster                                                      |
| thrift                  | 1.03 ms                                                | 743 us: 1.39x faster                                                       |
| regex_compile           | 177 ms                                                 | 128 ms: 1.39x faster                                                       |
| logging_simple          | 8.10 us                                                | 5.83 us: 1.39x faster                                                      |
| scimark_fft             | 421 ms                                                 | 304 ms: 1.39x faster                                                       |
| logging_format          | 8.85 us                                                | 6.42 us: 1.38x faster                                                      |
| unpack_sequence         | 59.4 ns                                                | 43.5 ns: 1.36x faster                                                      |
| tornado_http            | 128 ms                                                 | 94.3 ms: 1.36x faster                                                      |
| async_tree_none         | 711 ms                                                 | 526 ms: 1.35x faster                                                       |
| fannkuch                | 488 ms                                                 | 361 ms: 1.35x faster                                                       |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.34x faster                                                     |
| pycparser               | 1.53 sec                                               | 1.14 sec: 1.34x faster                                                     |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.34x faster                                                      |
| 2to3                    | 335 ms                                                 | 251 ms: 1.34x faster                                                       |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.08 ms: 1.34x faster                                                      |
| genshi_xml              | 63.7 ms                                                | 47.8 ms: 1.33x faster                                                      |
| deepcopy                | 438 us                                                 | 329 us: 1.33x faster                                                       |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.32x faster                                                      |
| nqueens                 | 100 ms                                                 | 75.8 ms: 1.32x faster                                                      |
| deepcopy_reduce         | 3.79 us                                                | 2.91 us: 1.30x faster                                                      |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.29x faster                                                       |
| async_tree_memoization  | 855 ms                                                 | 667 ms: 1.28x faster                                                       |
| sqlglot_optimize        | 65.2 ms                                                | 50.9 ms: 1.28x faster                                                      |
| docutils                | 3.18 sec                                               | 2.49 sec: 1.27x faster                                                     |
| async_tree_cpu_io_mixed | 949 ms                                                 | 755 ms: 1.26x faster                                                       |
| coroutines              | 31.6 ms                                                | 25.5 ms: 1.24x faster                                                      |
| xml_etree_generate      | 93.8 ms                                                | 76.7 ms: 1.22x faster                                                      |
| bench_thread_pool       | 946 us                                                 | 777 us: 1.22x faster                                                       |
| sympy_integrate         | 24.0 ms                                                | 19.8 ms: 1.21x faster                                                      |
| async_generators        | 426 ms                                                 | 354 ms: 1.20x faster                                                       |
| sympy_str               | 325 ms                                                 | 271 ms: 1.20x faster                                                       |
| json_loads              | 28.7 us                                                | 23.9 us: 1.20x faster                                                      |
| dulwich_log             | 75.8 ms                                                | 63.3 ms: 1.20x faster                                                      |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.18x faster                                                       |
| sympy_expand            | 534 ms                                                 | 455 ms: 1.17x faster                                                       |
| json                    | 5.35 ms                                                | 4.60 ms: 1.16x faster                                                      |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.16x faster                                                      |
| pickle_list             | 4.72 us                                                | 4.15 us: 1.14x faster                                                      |
| djangocms               | 36.9 us                                                | 32.4 us: 1.14x faster                                                      |
| create_gc_cycles        | 1.65 ms                                                | 1.46 ms: 1.13x faster                                                      |
| sqlite_synth            | 2.92 us                                                | 2.60 us: 1.12x faster                                                      |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                       |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                       |
| unpickle                | 14.2 us                                                | 13.1 us: 1.08x faster                                                      |
| meteor_contest          | 114 ms                                                 | 106 ms: 1.08x faster                                                       |
| mdp                     | 2.74 sec                                               | 2.56 sec: 1.07x faster                                                     |
| telco                   | 6.73 ms                                                | 6.33 ms: 1.06x faster                                                      |
| regex_dna               | 214 ms                                                 | 210 ms: 1.02x faster                                                       |
| pickle                  | 10.2 us                                                | 10.3 us: 1.01x slower                                                      |
| generators              | 76.4 ms                                                | 78.1 ms: 1.02x slower                                                      |
| unpickle_list           | 4.92 us                                                | 5.07 us: 1.03x slower                                                      |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                       |
| regex_effbot            | 3.19 ms                                                | 3.40 ms: 1.07x slower                                                      |
| python_startup_no_site  | 5.78 ms                                                | 6.25 ms: 1.08x slower                                                      |
| pickle_dict             | 27.6 us                                                | 31.0 us: 1.13x slower                                                      |
| dask                    | 436 ms                                                 | 499 ms: 1.14x slower                                                       |
| gc_traversal            | 3.53 ms                                                | 4.06 ms: 1.15x slower                                                      |
| coverage                | 74.7 ms                                                | 99.5 ms: 1.33x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                               |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230202-3.12.0a4+-fa5965d/bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d.json: mypy
