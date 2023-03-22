
# Results vs. 3.10.4

- fork: python
- ref: ed7c3ff15680c1939fad
- machine: darwin-arm64
- commit hash: ed7c3ff
- commit date: 2022-09-11
- overall geometric mean: 1.24x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 181 ms: 1.11x faster                                                   |
| chameleon      | 5.79 ms                                                | 4.63 ms: 1.25x faster                                                  |
| docutils       | 1.78 sec                                               | 1.46 sec: 1.22x faster                                                 |
| html5lib       | 44.2 ms                                                | 34.7 ms: 1.27x faster                                                  |
| tornado_http   | 91.5 ms                                                | 70.0 ms: 1.31x faster                                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 65.5 ms: 1.42x faster                                                  |
| float          | 72.4 ms                                                | 52.9 ms: 1.37x faster                                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 76.4 ms: 1.26x faster                                                  |
| regex_v8       | 17.6 ms                                                | 16.4 ms: 1.07x faster                                                  |
| regex_dna      | 162 ms                                                 | 152 ms: 1.07x faster                                                   |
| regex_effbot   | 2.46 ms                                                | 2.63 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 199 us: 1.42x faster                                                   |
| unpickle_pure_python | 203 us                                                 | 159 us: 1.28x faster                                                   |
| xml_etree_process    | 44.8 ms                                                | 35.1 ms: 1.28x faster                                                  |
| xml_etree_generate   | 54.2 ms                                                | 48.3 ms: 1.12x faster                                                  |
| json_dumps           | 8.40 ms                                                | 7.58 ms: 1.11x faster                                                  |
| xml_etree_iterparse  | 72.3 ms                                                | 65.7 ms: 1.10x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 99.5 ms: 1.07x faster                                                  |
| json_loads           | 16.9 us                                                | 16.2 us: 1.04x faster                                                  |
| pickle               | 7.35 us                                                | 7.22 us: 1.02x faster                                                  |
| unpickle_list        | 2.69 us                                                | 2.64 us: 1.02x faster                                                  |
| unpickle             | 9.89 us                                                | 9.74 us: 1.01x faster                                                  |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.01x slower                                                  |
| pickle_list          | 2.80 us                                                | 2.85 us: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 9.21 ms: 1.29x faster                                                  |
| python_startup_no_site | 8.88 ms                                                | 7.27 ms: 1.22x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.26x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 27.3 ms                                                | 21.1 ms: 1.29x faster                                                  |
| mako            | 10.5 ms                                                | 8.39 ms: 1.25x faster                                                  |
| genshi_xml      | 37.2 ms                                                | 30.1 ms: 1.24x faster                                                  |
| genshi_text     | 18.4 ms                                                | 15.2 ms: 1.21x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.25x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.82 ms: 1.82x faster                                                  |
| logging_silent          | 119 ns                                                 | 67.5 ns: 1.77x faster                                                  |
| raytrace                | 325 ms                                                 | 207 ms: 1.57x faster                                                   |
| richards                | 51.4 ms                                                | 32.8 ms: 1.57x faster                                                  |
| scimark_monte_carlo     | 72.5 ms                                                | 46.8 ms: 1.55x faster                                                  |
| async_tree_memoization  | 490 ms                                                 | 317 ms: 1.55x faster                                                   |
| scimark_sor             | 126 ms                                                 | 83.0 ms: 1.52x faster                                                  |
| go                      | 165 ms                                                 | 109 ms: 1.52x faster                                                   |
| scimark_lu              | 109 ms                                                 | 72.3 ms: 1.51x faster                                                  |
| crypto_pyaes            | 78.1 ms                                                | 51.8 ms: 1.51x faster                                                  |
| async_tree_io           | 1.02 sec                                               | 698 ms: 1.46x faster                                                   |
| pyflate                 | 453 ms                                                 | 313 ms: 1.45x faster                                                   |
| sqlglot_parse           | 1.37 ms                                                | 953 us: 1.43x faster                                                   |
| nbody                   | 93.3 ms                                                | 65.5 ms: 1.42x faster                                                  |
| async_tree_none         | 400 ms                                                 | 281 ms: 1.42x faster                                                   |
| pickle_pure_python      | 283 us                                                 | 199 us: 1.42x faster                                                   |
| sqlglot_transpile       | 1.57 ms                                                | 1.11 ms: 1.41x faster                                                  |
| pathlib                 | 28.8 ms                                                | 20.8 ms: 1.38x faster                                                  |
| float                   | 72.4 ms                                                | 52.9 ms: 1.37x faster                                                  |
| thrift                  | 580 us                                                 | 429 us: 1.35x faster                                                   |
| chaos                   | 66.7 ms                                                | 49.3 ms: 1.35x faster                                                  |
| logging_simple          | 4.63 us                                                | 3.45 us: 1.34x faster                                                  |
| hexiom                  | 6.32 ms                                                | 4.72 ms: 1.34x faster                                                  |
| logging_format          | 4.97 us                                                | 3.73 us: 1.33x faster                                                  |
| spectral_norm           | 95.8 ms                                                | 72.7 ms: 1.32x faster                                                  |
| pycparser               | 916 ms                                                 | 696 ms: 1.32x faster                                                   |
| deepcopy_memo           | 34.4 us                                                | 26.3 us: 1.31x faster                                                  |
| tornado_http            | 91.5 ms                                                | 70.0 ms: 1.31x faster                                                  |
| pprint_safe_repr        | 606 ms                                                 | 467 ms: 1.30x faster                                                   |
| python_startup          | 11.9 ms                                                | 9.21 ms: 1.29x faster                                                  |
| pprint_pformat          | 1.23 sec                                               | 954 ms: 1.29x faster                                                   |
| django_template         | 27.3 ms                                                | 21.1 ms: 1.29x faster                                                  |
| dulwich_log             | 37.1 ms                                                | 29.0 ms: 1.28x faster                                                  |
| unpickle_pure_python    | 203 us                                                 | 159 us: 1.28x faster                                                   |
| xml_etree_process       | 44.8 ms                                                | 35.1 ms: 1.28x faster                                                  |
| html5lib                | 44.2 ms                                                | 34.7 ms: 1.27x faster                                                  |
| deepcopy                | 281 us                                                 | 222 us: 1.27x faster                                                   |
| async_tree_cpu_io_mixed | 669 ms                                                 | 529 ms: 1.27x faster                                                   |
| regex_compile           | 96.4 ms                                                | 76.4 ms: 1.26x faster                                                  |
| chameleon               | 5.79 ms                                                | 4.63 ms: 1.25x faster                                                  |
| mako                    | 10.5 ms                                                | 8.39 ms: 1.25x faster                                                  |
| deepcopy_reduce         | 2.37 us                                                | 1.90 us: 1.25x faster                                                  |
| genshi_xml              | 37.2 ms                                                | 30.1 ms: 1.24x faster                                                  |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.24 ms: 1.23x faster                                                  |
| gunicorn                | 1.35 ms                                                | 1.10 ms: 1.22x faster                                                  |
| python_startup_no_site  | 8.88 ms                                                | 7.27 ms: 1.22x faster                                                  |
| docutils                | 1.78 sec                                               | 1.46 sec: 1.22x faster                                                 |
| aiohttp                 | 1.27 ms                                                | 1.04 ms: 1.22x faster                                                  |
| sqlglot_optimize        | 38.0 ms                                                | 31.2 ms: 1.22x faster                                                  |
| genshi_text             | 18.4 ms                                                | 15.2 ms: 1.21x faster                                                  |
| flaskblogging           | 2.75 ms                                                | 2.28 ms: 1.21x faster                                                  |
| fannkuch                | 317 ms                                                 | 263 ms: 1.21x faster                                                   |
| async_generators        | 234 ms                                                 | 195 ms: 1.20x faster                                                   |
| sqlalchemy_declarative  | 74.9 ms                                                | 62.4 ms: 1.20x faster                                                  |
| bench_thread_pool       | 546 us                                                 | 458 us: 1.19x faster                                                   |
| pylint                  | 307 ms                                                 | 265 ms: 1.16x faster                                                   |
| sympy_integrate         | 13.3 ms                                                | 11.5 ms: 1.16x faster                                                  |
| generators              | 32.7 ms                                                | 28.4 ms: 1.15x faster                                                  |
| sqlglot_normalize       | 196 ms                                                 | 171 ms: 1.15x faster                                                   |
| nqueens                 | 68.2 ms                                                | 59.5 ms: 1.15x faster                                                  |
| scimark_fft             | 230 ms                                                 | 201 ms: 1.14x faster                                                   |
| coroutines              | 20.2 ms                                                | 17.6 ms: 1.14x faster                                                  |
| sqlite_synth            | 1.47 us                                                | 1.29 us: 1.14x faster                                                  |
| sympy_expand            | 275 ms                                                 | 242 ms: 1.14x faster                                                   |
| unpack_sequence         | 37.4 ns                                                | 33.1 ns: 1.13x faster                                                  |
| sympy_str               | 169 ms                                                 | 151 ms: 1.12x faster                                                   |
| xml_etree_generate      | 54.2 ms                                                | 48.3 ms: 1.12x faster                                                  |
| 2to3                    | 201 ms                                                 | 181 ms: 1.11x faster                                                   |
| json_dumps              | 8.40 ms                                                | 7.58 ms: 1.11x faster                                                  |
| xml_etree_iterparse     | 72.3 ms                                                | 65.7 ms: 1.10x faster                                                  |
| sympy_sum               | 93.6 ms                                                | 85.5 ms: 1.09x faster                                                  |
| json                    | 3.08 ms                                                | 2.83 ms: 1.09x faster                                                  |
| mdp                     | 1.66 sec                                               | 1.54 sec: 1.08x faster                                                 |
| xml_etree_parse         | 106 ms                                                 | 99.5 ms: 1.07x faster                                                  |
| telco                   | 3.63 ms                                                | 3.40 ms: 1.07x faster                                                  |
| scimark_sparse_mat_mult | 3.46 ms                                                | 3.24 ms: 1.07x faster                                                  |
| regex_v8                | 17.6 ms                                                | 16.4 ms: 1.07x faster                                                  |
| regex_dna               | 162 ms                                                 | 152 ms: 1.07x faster                                                   |
| meteor_contest          | 78.1 ms                                                | 74.0 ms: 1.06x faster                                                  |
| json_loads              | 16.9 us                                                | 16.2 us: 1.04x faster                                                  |
| pickle                  | 7.35 us                                                | 7.22 us: 1.02x faster                                                  |
| unpickle_list           | 2.69 us                                                | 2.64 us: 1.02x faster                                                  |
| unpickle                | 9.89 us                                                | 9.74 us: 1.01x faster                                                  |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.01x slower                                                  |
| pickle_list             | 2.80 us                                                | 2.85 us: 1.02x slower                                                  |
| bench_mp_pool           | 39.7 ms                                                | 41.9 ms: 1.06x slower                                                  |
| regex_effbot            | 2.46 ms                                                | 2.63 ms: 1.07x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.24x faster                                                           |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp, comprehensions, coverage, create_gc_cycles, dask, gc_traversal, mypy2
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220911-3.11.0rc2-ed7c3ff/bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff.json: mypy
