
# Results vs. 3.10.4

- fork: python
- ref: 594de165bf2f21d6b28e
- machine: darwin-arm64
- commit hash: 594de16
- commit date: 2022-11-28
- overall geometric mean: 1.18x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 166 ms: 1.21x faster                                                   |
| chameleon      | 5.79 ms                                                | 4.49 ms: 1.29x faster                                                  |
| docutils       | 1.78 sec                                               | 1.47 sec: 1.21x faster                                                 |
| html5lib       | 44.2 ms                                                | 36.2 ms: 1.22x faster                                                  |
| tornado_http   | 91.5 ms                                                | 71.1 ms: 1.29x faster                                                  |
| Geometric mean | (ref)                                                  | 1.24x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 64.7 ms: 1.44x faster                                                  |
| float          | 72.4 ms                                                | 56.9 ms: 1.27x faster                                                  |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.23x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 75.9 ms: 1.27x faster                                                  |
| regex_v8       | 17.6 ms                                                | 15.7 ms: 1.12x faster                                                  |
| regex_dna      | 162 ms                                                 | 149 ms: 1.08x faster                                                   |
| regex_effbot   | 2.46 ms                                                | 2.61 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 8.40 ms                                                | 6.08 ms: 1.38x faster                                                  |
| pickle_pure_python   | 283 us                                                 | 212 us: 1.34x faster                                                   |
| xml_etree_process    | 44.8 ms                                                | 35.4 ms: 1.27x faster                                                  |
| unpickle_pure_python | 203 us                                                 | 162 us: 1.26x faster                                                   |
| xml_etree_generate   | 54.2 ms                                                | 48.7 ms: 1.11x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 96.2 ms: 1.11x faster                                                  |
| unpickle_list        | 2.69 us                                                | 2.57 us: 1.04x faster                                                  |
| xml_etree_iterparse  | 72.3 ms                                                | 69.3 ms: 1.04x faster                                                  |
| json_loads           | 16.9 us                                                | 16.3 us: 1.04x faster                                                  |
| pickle_dict          | 17.9 us                                                | 17.8 us: 1.00x faster                                                  |
| pickle               | 7.35 us                                                | 7.61 us: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                           |

Benchmark hidden because not significant (2): unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 12.2 ms: 1.03x slower                                                  |
| python_startup_no_site | 8.88 ms                                                | 10.2 ms: 1.15x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.31 ms: 1.43x faster                                                  |
| django_template | 27.3 ms                                                | 21.4 ms: 1.27x faster                                                  |
| genshi_xml      | 37.2 ms                                                | 29.3 ms: 1.27x faster                                                  |
| genshi_text     | 18.4 ms                                                | 14.6 ms: 1.26x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.31x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.79 ms: 1.84x faster                                                  |
| logging_silent          | 119 ns                                                 | 64.9 ns: 1.84x faster                                                  |
| richards                | 51.4 ms                                                | 32.1 ms: 1.60x faster                                                  |
| scimark_lu              | 109 ms                                                 | 71.1 ms: 1.54x faster                                                  |
| async_tree_memoization  | 490 ms                                                 | 329 ms: 1.49x faster                                                   |
| raytrace                | 325 ms                                                 | 219 ms: 1.49x faster                                                   |
| crypto_pyaes            | 78.1 ms                                                | 53.5 ms: 1.46x faster                                                  |
| nbody                   | 93.3 ms                                                | 64.7 ms: 1.44x faster                                                  |
| mako                    | 10.5 ms                                                | 7.31 ms: 1.43x faster                                                  |
| go                      | 165 ms                                                 | 118 ms: 1.40x faster                                                   |
| async_tree_none         | 400 ms                                                 | 289 ms: 1.38x faster                                                   |
| json_dumps              | 8.40 ms                                                | 6.08 ms: 1.38x faster                                                  |
| sqlglot_parse           | 1.37 ms                                                | 994 us: 1.37x faster                                                   |
| async_tree_io           | 1.02 sec                                               | 747 ms: 1.36x faster                                                   |
| sqlglot_transpile       | 1.57 ms                                                | 1.17 ms: 1.35x faster                                                  |
| pickle_pure_python      | 283 us                                                 | 212 us: 1.34x faster                                                   |
| thrift                  | 580 us                                                 | 440 us: 1.32x faster                                                   |
| pycparser               | 916 ms                                                 | 697 ms: 1.31x faster                                                   |
| chaos                   | 66.7 ms                                                | 50.9 ms: 1.31x faster                                                  |
| spectral_norm           | 95.8 ms                                                | 73.7 ms: 1.30x faster                                                  |
| scimark_sor             | 126 ms                                                 | 97.5 ms: 1.29x faster                                                  |
| chameleon               | 5.79 ms                                                | 4.49 ms: 1.29x faster                                                  |
| logging_simple          | 4.63 us                                                | 3.59 us: 1.29x faster                                                  |
| scimark_monte_carlo     | 72.5 ms                                                | 56.2 ms: 1.29x faster                                                  |
| tornado_http            | 91.5 ms                                                | 71.1 ms: 1.29x faster                                                  |
| hexiom                  | 6.32 ms                                                | 4.93 ms: 1.28x faster                                                  |
| pyflate                 | 453 ms                                                 | 354 ms: 1.28x faster                                                   |
| logging_format          | 4.97 us                                                | 3.89 us: 1.28x faster                                                  |
| django_template         | 27.3 ms                                                | 21.4 ms: 1.27x faster                                                  |
| float                   | 72.4 ms                                                | 56.9 ms: 1.27x faster                                                  |
| regex_compile           | 96.4 ms                                                | 75.9 ms: 1.27x faster                                                  |
| xml_etree_process       | 44.8 ms                                                | 35.4 ms: 1.27x faster                                                  |
| genshi_xml              | 37.2 ms                                                | 29.3 ms: 1.27x faster                                                  |
| create_gc_cycles        | 880 us                                                 | 698 us: 1.26x faster                                                   |
| genshi_text             | 18.4 ms                                                | 14.6 ms: 1.26x faster                                                  |
| unpickle_pure_python    | 203 us                                                 | 162 us: 1.26x faster                                                   |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.77 ms: 1.25x faster                                                  |
| dulwich_log             | 37.1 ms                                                | 30.2 ms: 1.23x faster                                                  |
| html5lib                | 44.2 ms                                                | 36.2 ms: 1.22x faster                                                  |
| pprint_safe_repr        | 606 ms                                                 | 497 ms: 1.22x faster                                                   |
| pprint_pformat          | 1.23 sec                                               | 1.02 sec: 1.21x faster                                                 |
| async_tree_cpu_io_mixed | 669 ms                                                 | 552 ms: 1.21x faster                                                   |
| 2to3                    | 201 ms                                                 | 166 ms: 1.21x faster                                                   |
| docutils                | 1.78 sec                                               | 1.47 sec: 1.21x faster                                                 |
| sqlglot_optimize        | 38.0 ms                                                | 31.8 ms: 1.19x faster                                                  |
| scimark_fft             | 230 ms                                                 | 198 ms: 1.17x faster                                                   |
| mypy2                   | 307 ms                                                 | 263 ms: 1.16x faster                                                   |
| deepcopy_memo           | 34.4 us                                                | 29.6 us: 1.16x faster                                                  |
| dask                    | 265 ms                                                 | 229 ms: 1.16x faster                                                   |
| fannkuch                | 317 ms                                                 | 274 ms: 1.16x faster                                                   |
| bench_thread_pool       | 546 us                                                 | 472 us: 1.16x faster                                                   |
| deepcopy                | 281 us                                                 | 243 us: 1.15x faster                                                   |
| deepcopy_reduce         | 2.37 us                                                | 2.08 us: 1.14x faster                                                  |
| async_generators        | 234 ms                                                 | 205 ms: 1.14x faster                                                   |
| sympy_integrate         | 13.3 ms                                                | 11.8 ms: 1.13x faster                                                  |
| sqlglot_normalize       | 196 ms                                                 | 174 ms: 1.13x faster                                                   |
| regex_v8                | 17.6 ms                                                | 15.7 ms: 1.12x faster                                                  |
| sympy_expand            | 275 ms                                                 | 248 ms: 1.11x faster                                                   |
| xml_etree_generate      | 54.2 ms                                                | 48.7 ms: 1.11x faster                                                  |
| xml_etree_parse         | 106 ms                                                 | 96.2 ms: 1.11x faster                                                  |
| json                    | 3.08 ms                                                | 2.81 ms: 1.10x faster                                                  |
| nqueens                 | 68.2 ms                                                | 62.2 ms: 1.10x faster                                                  |
| sympy_str               | 169 ms                                                 | 155 ms: 1.09x faster                                                   |
| regex_dna               | 162 ms                                                 | 149 ms: 1.08x faster                                                   |
| mdp                     | 1.66 sec                                               | 1.54 sec: 1.08x faster                                                 |
| sympy_sum               | 93.6 ms                                                | 86.9 ms: 1.08x faster                                                  |
| pathlib                 | 28.8 ms                                                | 26.9 ms: 1.07x faster                                                  |
| telco                   | 3.63 ms                                                | 3.41 ms: 1.07x faster                                                  |
| sqlite_synth            | 1.47 us                                                | 1.39 us: 1.06x faster                                                  |
| unpickle_list           | 2.69 us                                                | 2.57 us: 1.04x faster                                                  |
| xml_etree_iterparse     | 72.3 ms                                                | 69.3 ms: 1.04x faster                                                  |
| json_loads              | 16.9 us                                                | 16.3 us: 1.04x faster                                                  |
| asyncio_tcp             | 670 ms                                                 | 652 ms: 1.03x faster                                                   |
| meteor_contest          | 78.1 ms                                                | 77.2 ms: 1.01x faster                                                  |
| coroutines              | 20.2 ms                                                | 20.0 ms: 1.01x faster                                                  |
| pickle_dict             | 17.9 us                                                | 17.8 us: 1.00x faster                                                  |
| pidigits                | 282 ms                                                 | 281 ms: 1.00x faster                                                   |
| gc_traversal            | 2.39 ms                                                | 2.42 ms: 1.01x slower                                                  |
| comprehensions          | 17.6 us                                                | 17.8 us: 1.01x slower                                                  |
| python_startup          | 11.9 ms                                                | 12.2 ms: 1.03x slower                                                  |
| generators              | 32.7 ms                                                | 33.7 ms: 1.03x slower                                                  |
| pickle                  | 7.35 us                                                | 7.61 us: 1.04x slower                                                  |
| regex_effbot            | 2.46 ms                                                | 2.61 ms: 1.06x slower                                                  |
| bench_mp_pool           | 39.7 ms                                                | 44.2 ms: 1.11x slower                                                  |
| python_startup_no_site  | 8.88 ms                                                | 10.2 ms: 1.15x slower                                                  |
| coverage                | 42.0 ms                                                | 57.5 ms: 1.37x slower                                                  |
| unpack_sequence         | 37.4 ns                                                | 62.0 ns: 1.66x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.18x faster                                                           |

Benchmark hidden because not significant (2): unpickle, pickle_list
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
