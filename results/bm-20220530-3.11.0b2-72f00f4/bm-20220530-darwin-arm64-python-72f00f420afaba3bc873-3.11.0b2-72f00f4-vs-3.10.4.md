
# Results vs. 3.10.4

- fork: python
- ref: 72f00f420afaba3bc873
- machine: darwin-arm64
- commit hash: 72f00f4
- commit date: 2022-05-30
- overall geometric mean: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 162 ms: 1.24x faster                                                  |
| chameleon      | 5.79 ms                                                | 4.68 ms: 1.24x faster                                                 |
| docutils       | 1.78 sec                                               | 1.46 sec: 1.22x faster                                                |
| html5lib       | 44.2 ms                                                | 35.9 ms: 1.23x faster                                                 |
| tornado_http   | 91.5 ms                                                | 72.0 ms: 1.27x faster                                                 |
| Geometric mean | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 63.7 ms: 1.46x faster                                                 |
| float          | 72.4 ms                                                | 55.8 ms: 1.30x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 77.6 ms: 1.24x faster                                                 |
| regex_v8       | 17.6 ms                                                | 16.1 ms: 1.09x faster                                                 |
| regex_dna      | 162 ms                                                 | 149 ms: 1.08x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.39 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process    | 44.8 ms                                                | 34.9 ms: 1.28x faster                                                 |
| pickle_pure_python   | 283 us                                                 | 221 us: 1.28x faster                                                  |
| unpickle_pure_python | 203 us                                                 | 175 us: 1.16x faster                                                  |
| xml_etree_generate   | 54.2 ms                                                | 48.3 ms: 1.12x faster                                                 |
| json_dumps           | 8.40 ms                                                | 7.69 ms: 1.09x faster                                                 |
| json_loads           | 16.9 us                                                | 16.1 us: 1.05x faster                                                 |
| pickle               | 7.35 us                                                | 7.05 us: 1.04x faster                                                 |
| pickle_dict          | 17.9 us                                                | 17.2 us: 1.04x faster                                                 |
| xml_etree_iterparse  | 72.3 ms                                                | 69.4 ms: 1.04x faster                                                 |
| pickle_list          | 2.80 us                                                | 2.75 us: 1.02x faster                                                 |
| unpickle             | 9.89 us                                                | 10.0 us: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 12.2 ms: 1.02x slower                                                 |
| python_startup_no_site | 8.88 ms                                                | 9.88 ms: 1.11x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 27.3 ms                                                | 21.0 ms: 1.30x faster                                                 |
| mako            | 10.5 ms                                                | 8.44 ms: 1.24x faster                                                 |
| genshi_xml      | 37.2 ms                                                | 30.6 ms: 1.21x faster                                                 |
| genshi_text     | 18.4 ms                                                | 15.5 ms: 1.18x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.23x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| logging_silent          | 119 ns                                                 | 65.4 ns: 1.83x faster                                                 |
| deltablue               | 5.14 ms                                                | 2.82 ms: 1.82x faster                                                 |
| scimark_sor             | 126 ms                                                 | 76.0 ms: 1.66x faster                                                 |
| raytrace                | 325 ms                                                 | 207 ms: 1.57x faster                                                  |
| go                      | 165 ms                                                 | 106 ms: 1.56x faster                                                  |
| richards                | 51.4 ms                                                | 33.5 ms: 1.54x faster                                                 |
| scimark_lu              | 109 ms                                                 | 71.2 ms: 1.54x faster                                                 |
| crypto_pyaes            | 78.1 ms                                                | 51.6 ms: 1.52x faster                                                 |
| scimark_monte_carlo     | 72.5 ms                                                | 48.9 ms: 1.48x faster                                                 |
| nbody                   | 93.3 ms                                                | 63.7 ms: 1.46x faster                                                 |
| pyflate                 | 453 ms                                                 | 315 ms: 1.44x faster                                                  |
| async_tree_io           | 1.02 sec                                               | 713 ms: 1.43x faster                                                  |
| async_tree_memoization  | 490 ms                                                 | 353 ms: 1.39x faster                                                  |
| async_tree_none         | 400 ms                                                 | 291 ms: 1.37x faster                                                  |
| chaos                   | 66.7 ms                                                | 49.3 ms: 1.35x faster                                                 |
| hexiom                  | 6.32 ms                                                | 4.70 ms: 1.34x faster                                                 |
| logging_simple          | 4.63 us                                                | 3.46 us: 1.34x faster                                                 |
| thrift                  | 580 us                                                 | 436 us: 1.33x faster                                                  |
| logging_format          | 4.97 us                                                | 3.74 us: 1.33x faster                                                 |
| spectral_norm           | 95.8 ms                                                | 72.4 ms: 1.32x faster                                                 |
| pycparser               | 916 ms                                                 | 698 ms: 1.31x faster                                                  |
| float                   | 72.4 ms                                                | 55.8 ms: 1.30x faster                                                 |
| django_template         | 27.3 ms                                                | 21.0 ms: 1.30x faster                                                 |
| xml_etree_process       | 44.8 ms                                                | 34.9 ms: 1.28x faster                                                 |
| pickle_pure_python      | 283 us                                                 | 221 us: 1.28x faster                                                  |
| tornado_http            | 91.5 ms                                                | 72.0 ms: 1.27x faster                                                 |
| mako                    | 10.5 ms                                                | 8.44 ms: 1.24x faster                                                 |
| regex_compile           | 96.4 ms                                                | 77.6 ms: 1.24x faster                                                 |
| 2to3                    | 201 ms                                                 | 162 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed | 669 ms                                                 | 540 ms: 1.24x faster                                                  |
| pprint_safe_repr        | 606 ms                                                 | 489 ms: 1.24x faster                                                  |
| chameleon               | 5.79 ms                                                | 4.68 ms: 1.24x faster                                                 |
| mypy2                   | 307 ms                                                 | 248 ms: 1.23x faster                                                  |
| html5lib                | 44.2 ms                                                | 35.9 ms: 1.23x faster                                                 |
| pprint_pformat          | 1.23 sec                                               | 1.01 sec: 1.23x faster                                                |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.26 ms: 1.22x faster                                                 |
| dulwich_log             | 37.1 ms                                                | 30.3 ms: 1.22x faster                                                 |
| docutils                | 1.78 sec                                               | 1.46 sec: 1.22x faster                                                |
| fannkuch                | 317 ms                                                 | 261 ms: 1.22x faster                                                  |
| genshi_xml              | 37.2 ms                                                | 30.6 ms: 1.21x faster                                                 |
| create_gc_cycles        | 880 us                                                 | 727 us: 1.21x faster                                                  |
| sqlalchemy_declarative  | 74.9 ms                                                | 62.0 ms: 1.21x faster                                                 |
| sqlglot_optimize        | 38.0 ms                                                | 31.5 ms: 1.21x faster                                                 |
| deepcopy_memo           | 34.4 us                                                | 28.5 us: 1.21x faster                                                 |
| aiohttp                 | 1.27 ms                                                | 1.06 ms: 1.20x faster                                                 |
| async_generators        | 234 ms                                                 | 197 ms: 1.19x faster                                                  |
| genshi_text             | 18.4 ms                                                | 15.5 ms: 1.18x faster                                                 |
| deepcopy                | 281 us                                                 | 238 us: 1.18x faster                                                  |
| gunicorn                | 1.35 ms                                                | 1.14 ms: 1.18x faster                                                 |
| generators              | 32.7 ms                                                | 27.9 ms: 1.17x faster                                                 |
| nqueens                 | 68.2 ms                                                | 58.3 ms: 1.17x faster                                                 |
| coroutines              | 20.2 ms                                                | 17.3 ms: 1.17x faster                                                 |
| dask                    | 265 ms                                                 | 228 ms: 1.16x faster                                                  |
| unpickle_pure_python    | 203 us                                                 | 175 us: 1.16x faster                                                  |
| sqlglot_transpile       | 1.57 ms                                                | 1.36 ms: 1.16x faster                                                 |
| deepcopy_reduce         | 2.37 us                                                | 2.05 us: 1.16x faster                                                 |
| unpack_sequence         | 37.4 ns                                                | 32.4 ns: 1.15x faster                                                 |
| scimark_fft             | 230 ms                                                 | 200 ms: 1.15x faster                                                  |
| sqlglot_normalize       | 196 ms                                                 | 171 ms: 1.15x faster                                                  |
| bench_thread_pool       | 546 us                                                 | 477 us: 1.15x faster                                                  |
| sympy_integrate         | 13.3 ms                                                | 11.6 ms: 1.14x faster                                                 |
| sqlglot_parse           | 1.37 ms                                                | 1.19 ms: 1.14x faster                                                 |
| pylint                  | 307 ms                                                 | 270 ms: 1.14x faster                                                  |
| sympy_sum               | 93.6 ms                                                | 82.8 ms: 1.13x faster                                                 |
| sympy_expand            | 275 ms                                                 | 244 ms: 1.13x faster                                                  |
| sympy_str               | 169 ms                                                 | 151 ms: 1.12x faster                                                  |
| xml_etree_generate      | 54.2 ms                                                | 48.3 ms: 1.12x faster                                                 |
| sqlite_synth            | 1.47 us                                                | 1.33 us: 1.11x faster                                                 |
| json_dumps              | 8.40 ms                                                | 7.69 ms: 1.09x faster                                                 |
| regex_v8                | 17.6 ms                                                | 16.1 ms: 1.09x faster                                                 |
| json                    | 3.08 ms                                                | 2.83 ms: 1.09x faster                                                 |
| mdp                     | 1.66 sec                                               | 1.53 sec: 1.09x faster                                                |
| regex_dna               | 162 ms                                                 | 149 ms: 1.08x faster                                                  |
| scimark_sparse_mat_mult | 3.46 ms                                                | 3.20 ms: 1.08x faster                                                 |
| telco                   | 3.63 ms                                                | 3.42 ms: 1.06x faster                                                 |
| pathlib                 | 28.8 ms                                                | 27.4 ms: 1.05x faster                                                 |
| json_loads              | 16.9 us                                                | 16.1 us: 1.05x faster                                                 |
| pickle                  | 7.35 us                                                | 7.05 us: 1.04x faster                                                 |
| pickle_dict             | 17.9 us                                                | 17.2 us: 1.04x faster                                                 |
| xml_etree_iterparse     | 72.3 ms                                                | 69.4 ms: 1.04x faster                                                 |
| asyncio_tcp             | 670 ms                                                 | 650 ms: 1.03x faster                                                  |
| regex_effbot            | 2.46 ms                                                | 2.39 ms: 1.03x faster                                                 |
| pickle_list             | 2.80 us                                                | 2.75 us: 1.02x faster                                                 |
| pidigits                | 282 ms                                                 | 281 ms: 1.01x faster                                                  |
| meteor_contest          | 78.1 ms                                                | 77.7 ms: 1.01x faster                                                 |
| gc_traversal            | 2.39 ms                                                | 2.41 ms: 1.01x slower                                                 |
| unpickle                | 9.89 us                                                | 10.0 us: 1.01x slower                                                 |
| python_startup          | 11.9 ms                                                | 12.2 ms: 1.02x slower                                                 |
| comprehensions          | 17.6 us                                                | 18.4 us: 1.05x slower                                                 |
| bench_mp_pool           | 39.7 ms                                                | 43.5 ms: 1.10x slower                                                 |
| python_startup_no_site  | 8.88 ms                                                | 9.88 ms: 1.11x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.20x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle_list
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: coverage, flaskblogging
