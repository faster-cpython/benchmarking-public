
# Results vs. 3.10.4

- fork: python
- ref: 594de165bf2f21d6b28e
- machine: darwin-arm64
- commit hash: 594de16
- commit date: 2022-11-28
- overall geometric mean: 1.20x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 186 ms: 1.08x faster                                                   |
| chameleon      | 5.79 ms                                                | 4.64 ms: 1.25x faster                                                  |
| docutils       | 1.78 sec                                               | 1.46 sec: 1.22x faster                                                 |
| html5lib       | 44.2 ms                                                | 36.1 ms: 1.23x faster                                                  |
| tornado_http   | 91.5 ms                                                | 68.3 ms: 1.34x faster                                                  |
| Geometric mean | (ref)                                                  | 1.22x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 65.0 ms: 1.44x faster                                                  |
| float          | 72.4 ms                                                | 56.4 ms: 1.28x faster                                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.23x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 75.9 ms: 1.27x faster                                                  |
| regex_v8       | 17.6 ms                                                | 16.0 ms: 1.10x faster                                                  |
| regex_dna      | 162 ms                                                 | 149 ms: 1.08x faster                                                   |
| regex_effbot   | 2.46 ms                                                | 2.61 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 8.40 ms                                                | 6.07 ms: 1.38x faster                                                  |
| pickle_pure_python   | 283 us                                                 | 210 us: 1.35x faster                                                   |
| xml_etree_process    | 44.8 ms                                                | 35.2 ms: 1.27x faster                                                  |
| unpickle_pure_python | 203 us                                                 | 161 us: 1.27x faster                                                   |
| xml_etree_parse      | 106 ms                                                 | 93.2 ms: 1.14x faster                                                  |
| xml_etree_generate   | 54.2 ms                                                | 48.7 ms: 1.11x faster                                                  |
| xml_etree_iterparse  | 72.3 ms                                                | 66.4 ms: 1.09x faster                                                  |
| unpickle_list        | 2.69 us                                                | 2.59 us: 1.04x faster                                                  |
| json_loads           | 16.9 us                                                | 16.4 us: 1.03x faster                                                  |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.00x slower                                                  |
| pickle_list          | 2.80 us                                                | 2.85 us: 1.01x slower                                                  |
| pickle               | 7.35 us                                                | 7.54 us: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 9.29 ms: 1.28x faster                                                  |
| python_startup_no_site | 8.88 ms                                                | 7.33 ms: 1.21x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 8.24 ms: 1.27x faster                                                  |
| django_template | 27.3 ms                                                | 21.6 ms: 1.26x faster                                                  |
| genshi_xml      | 37.2 ms                                                | 29.6 ms: 1.26x faster                                                  |
| genshi_text     | 18.4 ms                                                | 15.2 ms: 1.21x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.25x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| logging_silent          | 119 ns                                                 | 64.4 ns: 1.85x faster                                                  |
| deltablue               | 5.14 ms                                                | 2.81 ms: 1.83x faster                                                  |
| richards                | 51.4 ms                                                | 31.3 ms: 1.64x faster                                                  |
| scimark_lu              | 109 ms                                                 | 71.0 ms: 1.54x faster                                                  |
| async_tree_memoization  | 490 ms                                                 | 323 ms: 1.52x faster                                                   |
| raytrace                | 325 ms                                                 | 220 ms: 1.48x faster                                                   |
| crypto_pyaes            | 78.1 ms                                                | 53.4 ms: 1.46x faster                                                  |
| nbody                   | 93.3 ms                                                | 65.0 ms: 1.44x faster                                                  |
| async_tree_none         | 400 ms                                                 | 286 ms: 1.40x faster                                                   |
| pathlib                 | 28.8 ms                                                | 20.6 ms: 1.40x faster                                                  |
| go                      | 165 ms                                                 | 118 ms: 1.40x faster                                                   |
| async_tree_io           | 1.02 sec                                               | 733 ms: 1.39x faster                                                   |
| json_dumps              | 8.40 ms                                                | 6.07 ms: 1.38x faster                                                  |
| sqlglot_parse           | 1.37 ms                                                | 996 us: 1.37x faster                                                   |
| sqlglot_transpile       | 1.57 ms                                                | 1.17 ms: 1.35x faster                                                  |
| pickle_pure_python      | 283 us                                                 | 210 us: 1.35x faster                                                   |
| tornado_http            | 91.5 ms                                                | 68.3 ms: 1.34x faster                                                  |
| thrift                  | 580 us                                                 | 438 us: 1.32x faster                                                   |
| chaos                   | 66.7 ms                                                | 51.1 ms: 1.31x faster                                                  |
| pycparser               | 916 ms                                                 | 702 ms: 1.30x faster                                                   |
| spectral_norm           | 95.8 ms                                                | 73.7 ms: 1.30x faster                                                  |
| scimark_monte_carlo     | 72.5 ms                                                | 56.3 ms: 1.29x faster                                                  |
| float                   | 72.4 ms                                                | 56.4 ms: 1.28x faster                                                  |
| hexiom                  | 6.32 ms                                                | 4.93 ms: 1.28x faster                                                  |
| python_startup          | 11.9 ms                                                | 9.29 ms: 1.28x faster                                                  |
| logging_simple          | 4.63 us                                                | 3.62 us: 1.28x faster                                                  |
| xml_etree_process       | 44.8 ms                                                | 35.2 ms: 1.27x faster                                                  |
| pyflate                 | 453 ms                                                 | 356 ms: 1.27x faster                                                   |
| logging_format          | 4.97 us                                                | 3.91 us: 1.27x faster                                                  |
| mako                    | 10.5 ms                                                | 8.24 ms: 1.27x faster                                                  |
| regex_compile           | 96.4 ms                                                | 75.9 ms: 1.27x faster                                                  |
| scimark_sor             | 126 ms                                                 | 99.3 ms: 1.27x faster                                                  |
| dulwich_log             | 37.1 ms                                                | 29.3 ms: 1.27x faster                                                  |
| unpickle_pure_python    | 203 us                                                 | 161 us: 1.27x faster                                                   |
| django_template         | 27.3 ms                                                | 21.6 ms: 1.26x faster                                                  |
| genshi_xml              | 37.2 ms                                                | 29.6 ms: 1.26x faster                                                  |
| chameleon               | 5.79 ms                                                | 4.64 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed | 669 ms                                                 | 539 ms: 1.24x faster                                                   |
| pprint_safe_repr        | 606 ms                                                 | 491 ms: 1.23x faster                                                   |
| pprint_pformat          | 1.23 sec                                               | 1.00 sec: 1.23x faster                                                 |
| html5lib                | 44.2 ms                                                | 36.1 ms: 1.23x faster                                                  |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.83 ms: 1.22x faster                                                  |
| docutils                | 1.78 sec                                               | 1.46 sec: 1.22x faster                                                 |
| python_startup_no_site  | 8.88 ms                                                | 7.33 ms: 1.21x faster                                                  |
| genshi_text             | 18.4 ms                                                | 15.2 ms: 1.21x faster                                                  |
| sqlglot_optimize        | 38.0 ms                                                | 31.6 ms: 1.20x faster                                                  |
| bench_thread_pool       | 546 us                                                 | 456 us: 1.20x faster                                                   |
| deepcopy                | 281 us                                                 | 240 us: 1.17x faster                                                   |
| deepcopy_memo           | 34.4 us                                                | 29.5 us: 1.17x faster                                                  |
| deepcopy_reduce         | 2.37 us                                                | 2.04 us: 1.16x faster                                                  |
| scimark_fft             | 230 ms                                                 | 198 ms: 1.16x faster                                                   |
| fannkuch                | 317 ms                                                 | 276 ms: 1.15x faster                                                   |
| async_generators        | 234 ms                                                 | 204 ms: 1.15x faster                                                   |
| xml_etree_parse         | 106 ms                                                 | 93.2 ms: 1.14x faster                                                  |
| sqlglot_normalize       | 196 ms                                                 | 173 ms: 1.13x faster                                                   |
| sympy_integrate         | 13.3 ms                                                | 11.8 ms: 1.13x faster                                                  |
| sympy_expand            | 275 ms                                                 | 247 ms: 1.12x faster                                                   |
| xml_etree_generate      | 54.2 ms                                                | 48.7 ms: 1.11x faster                                                  |
| nqueens                 | 68.2 ms                                                | 61.9 ms: 1.10x faster                                                  |
| regex_v8                | 17.6 ms                                                | 16.0 ms: 1.10x faster                                                  |
| sympy_str               | 169 ms                                                 | 155 ms: 1.09x faster                                                   |
| xml_etree_iterparse     | 72.3 ms                                                | 66.4 ms: 1.09x faster                                                  |
| regex_dna               | 162 ms                                                 | 149 ms: 1.08x faster                                                   |
| 2to3                    | 201 ms                                                 | 186 ms: 1.08x faster                                                   |
| sympy_sum               | 93.6 ms                                                | 86.6 ms: 1.08x faster                                                  |
| mdp                     | 1.66 sec                                               | 1.54 sec: 1.08x faster                                                 |
| json                    | 3.08 ms                                                | 2.86 ms: 1.08x faster                                                  |
| telco                   | 3.63 ms                                                | 3.43 ms: 1.06x faster                                                  |
| unpickle_list           | 2.69 us                                                | 2.59 us: 1.04x faster                                                  |
| json_loads              | 16.9 us                                                | 16.4 us: 1.03x faster                                                  |
| sqlite_synth            | 1.47 us                                                | 1.43 us: 1.03x faster                                                  |
| meteor_contest          | 78.1 ms                                                | 77.2 ms: 1.01x faster                                                  |
| coroutines              | 20.2 ms                                                | 20.0 ms: 1.01x faster                                                  |
| pidigits                | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.00x slower                                                  |
| pickle_list             | 2.80 us                                                | 2.85 us: 1.01x slower                                                  |
| pickle                  | 7.35 us                                                | 7.54 us: 1.03x slower                                                  |
| generators              | 32.7 ms                                                | 34.1 ms: 1.04x slower                                                  |
| regex_effbot            | 2.46 ms                                                | 2.61 ms: 1.06x slower                                                  |
| bench_mp_pool           | 39.7 ms                                                | 42.1 ms: 1.06x slower                                                  |
| coverage                | 42.0 ms                                                | 58.2 ms: 1.38x slower                                                  |
| unpack_sequence         | 37.4 ns                                                | 62.7 ns: 1.68x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.20x faster                                                           |

Benchmark hidden because not significant (1): unpickle
Ignored benchmarks (12) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221128-3.12.0a2+-594de16/bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16.json: mypy
