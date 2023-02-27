
# Results vs. 3.10.4

- fork: python
- ref: e3c3f9fec099fe78d2f9
- machine: linux-x86_64
- commit hash: e3c3f9f
- commit date: 2023-02-27
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230227-linux-x86_64-python-e3c3f9fec099fe78d2f9-3.12.0a5+-e3c3f9f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 247 ms: 1.36x faster                                                   |
| chameleon      | 9.17 ms                                                | 6.37 ms: 1.44x faster                                                  |
| docutils       | 3.18 sec                                               | 2.55 sec: 1.25x faster                                                 |
| html5lib       | 85.9 ms                                                | 61.3 ms: 1.40x faster                                                  |
| tornado_http   | 128 ms                                                 | 94.2 ms: 1.36x faster                                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230227-linux-x86_64-python-e3c3f9fec099fe78d2f9-3.12.0a5+-e3c3f9f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 109 ms                                                 | 72.5 ms: 1.50x faster                                                  |
| nbody          | 144 ms                                                 | 96.0 ms: 1.50x faster                                                  |
| pidigits       | 190 ms                                                 | 193 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230227-linux-x86_64-python-e3c3f9fec099fe78d2f9-3.12.0a5+-e3c3f9f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 131 ms: 1.35x faster                                                   |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.16x faster                                                  |
| regex_dna      | 214 ms                                                 | 198 ms: 1.08x faster                                                   |
| regex_effbot   | 3.19 ms                                                | 3.63 ms: 1.14x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230227-linux-x86_64-python-e3c3f9fec099fe78d2f9-3.12.0a5+-e3c3f9f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 280 us: 1.61x faster                                                   |
| unpickle_pure_python | 302 us                                                 | 195 us: 1.54x faster                                                   |
| json_dumps           | 13.4 ms                                                | 9.52 ms: 1.41x faster                                                  |
| xml_etree_process    | 74.5 ms                                                | 55.1 ms: 1.35x faster                                                  |
| json_loads           | 28.7 us                                                | 23.9 us: 1.20x faster                                                  |
| xml_etree_generate   | 93.8 ms                                                | 80.6 ms: 1.16x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 99.8 ms: 1.11x faster                                                  |
| pickle_list          | 4.72 us                                                | 4.33 us: 1.09x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 150 ms: 1.09x faster                                                   |
| unpickle             | 14.2 us                                                | 13.2 us: 1.07x faster                                                  |
| pickle               | 10.2 us                                                | 10.4 us: 1.02x slower                                                  |
| unpickle_list        | 4.92 us                                                | 5.08 us: 1.03x slower                                                  |
| pickle_dict          | 27.6 us                                                | 32.5 us: 1.18x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230227-linux-x86_64-python-e3c3f9fec099fe78d2f9-3.12.0a5+-e3c3f9f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.95 ms: 1.57x faster                                                  |
| python_startup_no_site | 5.78 ms                                                | 6.49 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230227-linux-x86_64-python-e3c3f9fec099fe78d2f9-3.12.0a5+-e3c3f9f |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.99 ms: 1.47x faster                                                  |
| genshi_text     | 30.6 ms                                                | 20.9 ms: 1.47x faster                                                  |
| django_template | 46.3 ms                                                | 32.5 ms: 1.43x faster                                                  |
| genshi_xml      | 63.7 ms                                                | 47.0 ms: 1.36x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230227-linux-x86_64-python-e3c3f9fec099fe78d2f9-3.12.0a5+-e3c3f9f |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 29.9 ms: 2.55x faster                                                  |
| deltablue               | 7.28 ms                                                | 3.11 ms: 2.34x faster                                                  |
| logging_silent          | 176 ns                                                 | 92.2 ns: 1.91x faster                                                  |
| scimark_sor             | 197 ms                                                 | 104 ms: 1.89x faster                                                   |
| richards                | 75.2 ms                                                | 41.0 ms: 1.84x faster                                                  |
| asyncio_tcp             | 914 ms                                                 | 503 ms: 1.82x faster                                                   |
| go                      | 226 ms                                                 | 132 ms: 1.70x faster                                                   |
| raytrace                | 467 ms                                                 | 280 ms: 1.67x faster                                                   |
| pyflate                 | 676 ms                                                 | 405 ms: 1.67x faster                                                   |
| crypto_pyaes            | 117 ms                                                 | 72.1 ms: 1.62x faster                                                  |
| pickle_pure_python      | 452 us                                                 | 280 us: 1.61x faster                                                   |
| spectral_norm           | 150 ms                                                 | 94.0 ms: 1.59x faster                                                  |
| scimark_monte_carlo     | 109 ms                                                 | 68.3 ms: 1.59x faster                                                  |
| python_startup          | 14.1 ms                                                | 8.95 ms: 1.57x faster                                                  |
| hexiom                  | 9.43 ms                                                | 6.00 ms: 1.57x faster                                                  |
| chaos                   | 106 ms                                                 | 68.2 ms: 1.55x faster                                                  |
| unpickle_pure_python    | 302 us                                                 | 195 us: 1.54x faster                                                   |
| float                   | 109 ms                                                 | 72.5 ms: 1.50x faster                                                  |
| nbody                   | 144 ms                                                 | 96.0 ms: 1.50x faster                                                  |
| deepcopy_memo           | 51.7 us                                                | 34.6 us: 1.49x faster                                                  |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.48x faster                                                   |
| mako                    | 14.7 ms                                                | 9.99 ms: 1.47x faster                                                  |
| genshi_text             | 30.6 ms                                                | 20.9 ms: 1.47x faster                                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.44x faster                                                  |
| chameleon               | 9.17 ms                                                | 6.37 ms: 1.44x faster                                                  |
| django_template         | 46.3 ms                                                | 32.5 ms: 1.43x faster                                                  |
| pprint_pformat          | 1.98 sec                                               | 1.39 sec: 1.42x faster                                                 |
| sqlglot_transpile       | 2.43 ms                                                | 1.71 ms: 1.42x faster                                                  |
| json_dumps              | 13.4 ms                                                | 9.52 ms: 1.41x faster                                                  |
| pycparser               | 1.53 sec                                               | 1.09 sec: 1.41x faster                                                 |
| unpack_sequence         | 59.4 ns                                                | 42.2 ns: 1.41x faster                                                  |
| pprint_safe_repr        | 953 ms                                                 | 680 ms: 1.40x faster                                                   |
| html5lib                | 85.9 ms                                                | 61.3 ms: 1.40x faster                                                  |
| logging_simple          | 8.10 us                                                | 5.79 us: 1.40x faster                                                  |
| logging_format          | 8.85 us                                                | 6.38 us: 1.39x faster                                                  |
| fannkuch                | 488 ms                                                 | 352 ms: 1.39x faster                                                   |
| async_tree_io           | 1.78 sec                                               | 1.30 sec: 1.37x faster                                                 |
| tornado_http            | 128 ms                                                 | 94.2 ms: 1.36x faster                                                  |
| thrift                  | 1.03 ms                                                | 761 us: 1.36x faster                                                   |
| async_tree_none         | 711 ms                                                 | 524 ms: 1.36x faster                                                   |
| genshi_xml              | 63.7 ms                                                | 47.0 ms: 1.36x faster                                                  |
| 2to3                    | 335 ms                                                 | 247 ms: 1.36x faster                                                   |
| xml_etree_process       | 74.5 ms                                                | 55.1 ms: 1.35x faster                                                  |
| regex_compile           | 177 ms                                                 | 131 ms: 1.35x faster                                                   |
| scimark_fft             | 421 ms                                                 | 313 ms: 1.35x faster                                                   |
| coroutines              | 31.6 ms                                                | 23.7 ms: 1.34x faster                                                  |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                                  |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.33x faster                                                  |
| async_tree_memoization  | 855 ms                                                 | 649 ms: 1.32x faster                                                   |
| deepcopy                | 438 us                                                 | 333 us: 1.32x faster                                                   |
| mypy2                   | 430 ms                                                 | 332 ms: 1.30x faster                                                   |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.30x faster                                                   |
| sqlglot_optimize        | 65.2 ms                                                | 50.8 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed | 949 ms                                                 | 743 ms: 1.28x faster                                                   |
| nqueens                 | 100 ms                                                 | 78.4 ms: 1.28x faster                                                  |
| deepcopy_reduce         | 3.79 us                                                | 3.02 us: 1.25x faster                                                  |
| docutils                | 3.18 sec                                               | 2.55 sec: 1.25x faster                                                 |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.48 ms: 1.22x faster                                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.22x faster                                                   |
| bench_thread_pool       | 946 us                                                 | 786 us: 1.20x faster                                                   |
| json_loads              | 28.7 us                                                | 23.9 us: 1.20x faster                                                  |
| dulwich_log             | 75.8 ms                                                | 63.3 ms: 1.20x faster                                                  |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.0 ms: 1.19x faster                                                  |
| json                    | 5.35 ms                                                | 4.53 ms: 1.18x faster                                                  |
| sympy_expand            | 534 ms                                                 | 455 ms: 1.17x faster                                                   |
| sympy_integrate         | 24.0 ms                                                | 20.5 ms: 1.17x faster                                                  |
| xml_etree_generate      | 93.8 ms                                                | 80.6 ms: 1.16x faster                                                  |
| sympy_str               | 325 ms                                                 | 281 ms: 1.16x faster                                                   |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.16x faster                                                  |
| djangocms               | 36.9 us                                                | 31.9 us: 1.16x faster                                                  |
| create_gc_cycles        | 1.65 ms                                                | 1.47 ms: 1.12x faster                                                  |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                  |
| sympy_sum               | 183 ms                                                 | 165 ms: 1.11x faster                                                   |
| xml_etree_iterparse     | 111 ms                                                 | 99.8 ms: 1.11x faster                                                  |
| sqlite_synth            | 2.92 us                                                | 2.64 us: 1.11x faster                                                  |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.10x faster                                                   |
| pickle_list             | 4.72 us                                                | 4.33 us: 1.09x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 150 ms: 1.09x faster                                                   |
| regex_dna               | 214 ms                                                 | 198 ms: 1.08x faster                                                   |
| unpickle                | 14.2 us                                                | 13.2 us: 1.07x faster                                                  |
| async_generators        | 426 ms                                                 | 409 ms: 1.04x faster                                                   |
| telco                   | 6.73 ms                                                | 6.53 ms: 1.03x faster                                                  |
| mdp                     | 2.74 sec                                               | 2.69 sec: 1.02x faster                                                 |
| pidigits                | 190 ms                                                 | 193 ms: 1.02x slower                                                   |
| pickle                  | 10.2 us                                                | 10.4 us: 1.02x slower                                                  |
| unpickle_list           | 4.92 us                                                | 5.08 us: 1.03x slower                                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.49 ms: 1.12x slower                                                  |
| regex_effbot            | 3.19 ms                                                | 3.63 ms: 1.14x slower                                                  |
| dask                    | 436 ms                                                 | 498 ms: 1.14x slower                                                   |
| pickle_dict             | 27.6 us                                                | 32.5 us: 1.18x slower                                                  |
| gc_traversal            | 3.53 ms                                                | 4.30 ms: 1.22x slower                                                  |
| coverage                | 74.7 ms                                                | 96.5 ms: 1.29x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
