
# Results vs. 3.10.4

- fork: faster-cpython
- ref: restrict_for_iter_sp
- machine: linux-x86_64
- commit hash: fb5f321
- commit date: 2023-02-17
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-faster%2dcpython-restrict_for_iter_sp-3.12.0a5+-fb5f321 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 247 ms: 1.36x faster                                                             |
| chameleon      | 9.17 ms                                                | 6.39 ms: 1.43x faster                                                            |
| docutils       | 3.18 sec                                               | 2.53 sec: 1.26x faster                                                           |
| html5lib       | 85.9 ms                                                | 61.2 ms: 1.40x faster                                                            |
| tornado_http   | 128 ms                                                 | 94.8 ms: 1.35x faster                                                            |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-faster%2dcpython-restrict_for_iter_sp-3.12.0a5+-fb5f321 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 95.5 ms: 1.51x faster                                                            |
| float          | 109 ms                                                 | 73.7 ms: 1.48x faster                                                            |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                             |
| Geometric mean | (ref)                                                  | 1.29x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-faster%2dcpython-restrict_for_iter_sp-3.12.0a5+-fb5f321 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 132 ms: 1.34x faster                                                             |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                            |
| regex_dna      | 214 ms                                                 | 199 ms: 1.08x faster                                                             |
| regex_effbot   | 3.19 ms                                                | 3.65 ms: 1.14x slower                                                            |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-faster%2dcpython-restrict_for_iter_sp-3.12.0a5+-fb5f321 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 281 us: 1.61x faster                                                             |
| unpickle_pure_python | 302 us                                                 | 197 us: 1.53x faster                                                             |
| json_dumps           | 13.4 ms                                                | 9.50 ms: 1.42x faster                                                            |
| xml_etree_process    | 74.5 ms                                                | 55.7 ms: 1.34x faster                                                            |
| json_loads           | 28.7 us                                                | 24.0 us: 1.20x faster                                                            |
| pickle_list          | 4.72 us                                                | 4.01 us: 1.18x faster                                                            |
| xml_etree_generate   | 93.8 ms                                                | 81.2 ms: 1.15x faster                                                            |
| xml_etree_iterparse  | 111 ms                                                 | 99.7 ms: 1.11x faster                                                            |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                             |
| pickle               | 10.2 us                                                | 9.98 us: 1.02x faster                                                            |
| unpickle_list        | 4.92 us                                                | 5.04 us: 1.02x slower                                                            |
| pickle_dict          | 27.6 us                                                | 30.2 us: 1.09x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                     |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-faster%2dcpython-restrict_for_iter_sp-3.12.0a5+-fb5f321 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.92 ms: 1.58x faster                                                            |
| python_startup_no_site | 5.78 ms                                                | 6.47 ms: 1.12x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-faster%2dcpython-restrict_for_iter_sp-3.12.0a5+-fb5f321 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.89 ms: 1.48x faster                                                            |
| genshi_text     | 30.6 ms                                                | 21.2 ms: 1.44x faster                                                            |
| django_template | 46.3 ms                                                | 33.0 ms: 1.40x faster                                                            |
| genshi_xml      | 63.7 ms                                                | 48.4 ms: 1.32x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-faster%2dcpython-restrict_for_iter_sp-3.12.0a5+-fb5f321 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 30.6 ms: 2.50x faster                                                            |
| deltablue               | 7.28 ms                                                | 3.19 ms: 2.28x faster                                                            |
| logging_silent          | 176 ns                                                 | 95.7 ns: 1.84x faster                                                            |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                             |
| asyncio_tcp             | 914 ms                                                 | 504 ms: 1.81x faster                                                             |
| richards                | 75.2 ms                                                | 42.2 ms: 1.78x faster                                                            |
| go                      | 226 ms                                                 | 134 ms: 1.68x faster                                                             |
| pyflate                 | 676 ms                                                 | 402 ms: 1.68x faster                                                             |
| scimark_monte_carlo     | 109 ms                                                 | 67.1 ms: 1.62x faster                                                            |
| pickle_pure_python      | 452 us                                                 | 281 us: 1.61x faster                                                             |
| raytrace                | 467 ms                                                 | 290 ms: 1.61x faster                                                             |
| spectral_norm           | 150 ms                                                 | 94.1 ms: 1.59x faster                                                            |
| python_startup          | 14.1 ms                                                | 8.92 ms: 1.58x faster                                                            |
| crypto_pyaes            | 117 ms                                                 | 74.2 ms: 1.57x faster                                                            |
| chaos                   | 106 ms                                                 | 68.0 ms: 1.55x faster                                                            |
| unpickle_pure_python    | 302 us                                                 | 197 us: 1.53x faster                                                             |
| nbody                   | 144 ms                                                 | 95.5 ms: 1.51x faster                                                            |
| hexiom                  | 9.43 ms                                                | 6.27 ms: 1.50x faster                                                            |
| deepcopy_memo           | 51.7 us                                                | 34.6 us: 1.49x faster                                                            |
| mako                    | 14.7 ms                                                | 9.89 ms: 1.48x faster                                                            |
| float                   | 109 ms                                                 | 73.7 ms: 1.48x faster                                                            |
| scimark_lu              | 161 ms                                                 | 110 ms: 1.46x faster                                                             |
| genshi_text             | 30.6 ms                                                | 21.2 ms: 1.44x faster                                                            |
| chameleon               | 9.17 ms                                                | 6.39 ms: 1.43x faster                                                            |
| coroutines              | 31.6 ms                                                | 22.1 ms: 1.43x faster                                                            |
| sqlglot_parse           | 2.04 ms                                                | 1.44 ms: 1.42x faster                                                            |
| unpack_sequence         | 59.4 ns                                                | 41.9 ns: 1.42x faster                                                            |
| json_dumps              | 13.4 ms                                                | 9.50 ms: 1.42x faster                                                            |
| logging_simple          | 8.10 us                                                | 5.74 us: 1.41x faster                                                            |
| pprint_pformat          | 1.98 sec                                               | 1.41 sec: 1.41x faster                                                           |
| html5lib                | 85.9 ms                                                | 61.2 ms: 1.40x faster                                                            |
| sqlglot_transpile       | 2.43 ms                                                | 1.73 ms: 1.40x faster                                                            |
| django_template         | 46.3 ms                                                | 33.0 ms: 1.40x faster                                                            |
| pprint_safe_repr        | 953 ms                                                 | 680 ms: 1.40x faster                                                             |
| pycparser               | 1.53 sec                                               | 1.10 sec: 1.40x faster                                                           |
| logging_format          | 8.85 us                                                | 6.37 us: 1.39x faster                                                            |
| 2to3                    | 335 ms                                                 | 247 ms: 1.36x faster                                                             |
| tornado_http            | 128 ms                                                 | 94.8 ms: 1.35x faster                                                            |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                                           |
| fannkuch                | 488 ms                                                 | 362 ms: 1.35x faster                                                             |
| thrift                  | 1.03 ms                                                | 769 us: 1.34x faster                                                             |
| async_tree_none         | 711 ms                                                 | 529 ms: 1.34x faster                                                             |
| scimark_fft             | 421 ms                                                 | 314 ms: 1.34x faster                                                             |
| regex_compile           | 177 ms                                                 | 132 ms: 1.34x faster                                                             |
| xml_etree_process       | 74.5 ms                                                | 55.7 ms: 1.34x faster                                                            |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                                            |
| genshi_xml              | 63.7 ms                                                | 48.4 ms: 1.32x faster                                                            |
| deepcopy                | 438 us                                                 | 333 us: 1.31x faster                                                             |
| gunicorn                | 1.43 ms                                                | 1.10 ms: 1.30x faster                                                            |
| mypy2                   | 430 ms                                                 | 331 ms: 1.30x faster                                                             |
| deepcopy_reduce         | 3.79 us                                                | 2.94 us: 1.29x faster                                                            |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                             |
| sqlglot_optimize        | 65.2 ms                                                | 51.1 ms: 1.28x faster                                                            |
| async_tree_memoization  | 855 ms                                                 | 677 ms: 1.26x faster                                                             |
| async_tree_cpu_io_mixed | 949 ms                                                 | 752 ms: 1.26x faster                                                             |
| docutils                | 3.18 sec                                               | 2.53 sec: 1.26x faster                                                           |
| nqueens                 | 100 ms                                                 | 81.7 ms: 1.22x faster                                                            |
| dulwich_log             | 75.8 ms                                                | 62.8 ms: 1.21x faster                                                            |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.21x faster                                                             |
| sympy_integrate         | 24.0 ms                                                | 20.0 ms: 1.20x faster                                                            |
| bench_thread_pool       | 946 us                                                 | 791 us: 1.20x faster                                                             |
| json_loads              | 28.7 us                                                | 24.0 us: 1.20x faster                                                            |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.0 ms: 1.19x faster                                                            |
| sympy_str               | 325 ms                                                 | 273 ms: 1.19x faster                                                             |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.60 ms: 1.19x faster                                                            |
| pickle_list             | 4.72 us                                                | 4.01 us: 1.18x faster                                                            |
| sympy_expand            | 534 ms                                                 | 455 ms: 1.17x faster                                                             |
| json                    | 5.35 ms                                                | 4.60 ms: 1.16x faster                                                            |
| xml_etree_generate      | 93.8 ms                                                | 81.2 ms: 1.15x faster                                                            |
| sympy_sum               | 183 ms                                                 | 159 ms: 1.15x faster                                                             |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                            |
| djangocms               | 36.9 us                                                | 32.4 us: 1.14x faster                                                            |
| create_gc_cycles        | 1.65 ms                                                | 1.48 ms: 1.12x faster                                                            |
| xml_etree_iterparse     | 111 ms                                                 | 99.7 ms: 1.11x faster                                                            |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.11x faster                                                             |
| pathlib                 | 20.0 ms                                                | 18.1 ms: 1.10x faster                                                            |
| sqlite_synth            | 2.92 us                                                | 2.66 us: 1.10x faster                                                            |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                             |
| regex_dna               | 214 ms                                                 | 199 ms: 1.08x faster                                                             |
| async_generators        | 426 ms                                                 | 410 ms: 1.04x faster                                                             |
| mdp                     | 2.74 sec                                               | 2.66 sec: 1.03x faster                                                           |
| telco                   | 6.73 ms                                                | 6.58 ms: 1.02x faster                                                            |
| pickle                  | 10.2 us                                                | 9.98 us: 1.02x faster                                                            |
| unpickle_list           | 4.92 us                                                | 5.04 us: 1.02x slower                                                            |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                             |
| pickle_dict             | 27.6 us                                                | 30.2 us: 1.09x slower                                                            |
| python_startup_no_site  | 5.78 ms                                                | 6.47 ms: 1.12x slower                                                            |
| regex_effbot            | 3.19 ms                                                | 3.65 ms: 1.14x slower                                                            |
| dask                    | 436 ms                                                 | 502 ms: 1.15x slower                                                             |
| coverage                | 74.7 ms                                                | 97.9 ms: 1.31x slower                                                            |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                     |

Benchmark hidden because not significant (3): unpickle, bench_mp_pool, gc_traversal
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
