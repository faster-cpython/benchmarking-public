
# Results vs. 3.10.4

- fork: python
- ref: 7b14c2ef194b6eed7967
- machine: darwin-arm64
- commit hash: 7b14c2e
- commit date: 2023-01-16
- overall geometric mean: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-darwin-arm64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 163 ms: 1.24x faster                                                   |
| chameleon      | 5.79 ms                                                | 4.57 ms: 1.27x faster                                                  |
| docutils       | 1.78 sec                                               | 1.46 sec: 1.22x faster                                                 |
| html5lib       | 44.2 ms                                                | 34.9 ms: 1.27x faster                                                  |
| tornado_http   | 91.5 ms                                                | 70.5 ms: 1.30x faster                                                  |
| Geometric mean | (ref)                                                  | 1.26x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-darwin-arm64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 64.1 ms: 1.46x faster                                                  |
| float          | 72.4 ms                                                | 51.7 ms: 1.40x faster                                                  |
| pidigits       | 282 ms                                                 | 281 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.27x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-darwin-arm64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 74.6 ms: 1.29x faster                                                  |
| regex_v8       | 17.6 ms                                                | 15.7 ms: 1.12x faster                                                  |
| regex_dna      | 162 ms                                                 | 149 ms: 1.08x faster                                                   |
| regex_effbot   | 2.46 ms                                                | 2.62 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-darwin-arm64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 193 us: 1.47x faster                                                   |
| unpickle_pure_python | 203 us                                                 | 144 us: 1.41x faster                                                   |
| json_dumps           | 8.40 ms                                                | 6.15 ms: 1.37x faster                                                  |
| xml_etree_process    | 44.8 ms                                                | 35.0 ms: 1.28x faster                                                  |
| xml_etree_generate   | 54.2 ms                                                | 48.2 ms: 1.12x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 96.9 ms: 1.10x faster                                                  |
| json_loads           | 16.9 us                                                | 16.2 us: 1.05x faster                                                  |
| xml_etree_iterparse  | 72.3 ms                                                | 70.1 ms: 1.03x faster                                                  |
| unpickle             | 9.89 us                                                | 9.74 us: 1.01x faster                                                  |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.00x slower                                                  |
| unpickle_list        | 2.69 us                                                | 2.73 us: 1.01x slower                                                  |
| pickle_list          | 2.80 us                                                | 2.85 us: 1.02x slower                                                  |
| pickle               | 7.35 us                                                | 7.50 us: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-darwin-arm64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 12.4 ms: 1.04x slower                                                  |
| python_startup_no_site | 8.88 ms                                                | 10.4 ms: 1.17x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-darwin-arm64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 37.2 ms                                                | 28.2 ms: 1.32x faster                                                  |
| mako            | 10.5 ms                                                | 8.14 ms: 1.29x faster                                                  |
| django_template | 27.3 ms                                                | 21.7 ms: 1.26x faster                                                  |
| genshi_text     | 18.4 ms                                                | 15.2 ms: 1.21x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.27x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-darwin-arm64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.63 ms: 1.95x faster                                                  |
| logging_silent          | 119 ns                                                 | 66.1 ns: 1.80x faster                                                  |
| richards                | 51.4 ms                                                | 30.8 ms: 1.67x faster                                                  |
| scimark_sor             | 126 ms                                                 | 78.5 ms: 1.61x faster                                                  |
| go                      | 165 ms                                                 | 108 ms: 1.53x faster                                                   |
| scimark_lu              | 109 ms                                                 | 72.6 ms: 1.51x faster                                                  |
| raytrace                | 325 ms                                                 | 219 ms: 1.49x faster                                                   |
| crypto_pyaes            | 78.1 ms                                                | 52.9 ms: 1.48x faster                                                  |
| async_tree_memoization  | 490 ms                                                 | 332 ms: 1.48x faster                                                   |
| pickle_pure_python      | 283 us                                                 | 193 us: 1.47x faster                                                   |
| nbody                   | 93.3 ms                                                | 64.1 ms: 1.46x faster                                                  |
| scimark_monte_carlo     | 72.5 ms                                                | 49.8 ms: 1.45x faster                                                  |
| asyncio_tcp             | 670 ms                                                 | 464 ms: 1.44x faster                                                   |
| pyflate                 | 453 ms                                                 | 316 ms: 1.43x faster                                                   |
| unpickle_pure_python    | 203 us                                                 | 144 us: 1.41x faster                                                   |
| float                   | 72.4 ms                                                | 51.7 ms: 1.40x faster                                                  |
| async_tree_none         | 400 ms                                                 | 289 ms: 1.39x faster                                                   |
| json_dumps              | 8.40 ms                                                | 6.15 ms: 1.37x faster                                                  |
| pycparser               | 916 ms                                                 | 673 ms: 1.36x faster                                                   |
| async_tree_io           | 1.02 sec                                               | 750 ms: 1.36x faster                                                   |
| deepcopy_memo           | 34.4 us                                                | 26.0 us: 1.32x faster                                                  |
| logging_simple          | 4.63 us                                                | 3.49 us: 1.32x faster                                                  |
| thrift                  | 580 us                                                 | 440 us: 1.32x faster                                                   |
| hexiom                  | 6.32 ms                                                | 4.79 ms: 1.32x faster                                                  |
| genshi_xml              | 37.2 ms                                                | 28.2 ms: 1.32x faster                                                  |
| chaos                   | 66.7 ms                                                | 50.7 ms: 1.32x faster                                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.04 ms: 1.32x faster                                                  |
| sqlglot_transpile       | 1.57 ms                                                | 1.20 ms: 1.31x faster                                                  |
| logging_format          | 4.97 us                                                | 3.80 us: 1.31x faster                                                  |
| pprint_pformat          | 1.23 sec                                               | 945 ms: 1.30x faster                                                   |
| pprint_safe_repr        | 606 ms                                                 | 465 ms: 1.30x faster                                                   |
| spectral_norm           | 95.8 ms                                                | 73.7 ms: 1.30x faster                                                  |
| tornado_http            | 91.5 ms                                                | 70.5 ms: 1.30x faster                                                  |
| regex_compile           | 96.4 ms                                                | 74.6 ms: 1.29x faster                                                  |
| mako                    | 10.5 ms                                                | 8.14 ms: 1.29x faster                                                  |
| xml_etree_process       | 44.8 ms                                                | 35.0 ms: 1.28x faster                                                  |
| chameleon               | 5.79 ms                                                | 4.57 ms: 1.27x faster                                                  |
| html5lib                | 44.2 ms                                                | 34.9 ms: 1.27x faster                                                  |
| deepcopy                | 281 us                                                 | 223 us: 1.26x faster                                                   |
| create_gc_cycles        | 880 us                                                 | 700 us: 1.26x faster                                                   |
| django_template         | 27.3 ms                                                | 21.7 ms: 1.26x faster                                                  |
| dulwich_log             | 37.1 ms                                                | 29.7 ms: 1.25x faster                                                  |
| fannkuch                | 317 ms                                                 | 254 ms: 1.25x faster                                                   |
| deepcopy_reduce         | 2.37 us                                                | 1.91 us: 1.24x faster                                                  |
| 2to3                    | 201 ms                                                 | 163 ms: 1.24x faster                                                   |
| async_tree_cpu_io_mixed | 669 ms                                                 | 543 ms: 1.23x faster                                                   |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.80 ms: 1.23x faster                                                  |
| docutils                | 1.78 sec                                               | 1.46 sec: 1.22x faster                                                 |
| sqlglot_optimize        | 38.0 ms                                                | 31.4 ms: 1.21x faster                                                  |
| genshi_text             | 18.4 ms                                                | 15.2 ms: 1.21x faster                                                  |
| scimark_fft             | 230 ms                                                 | 195 ms: 1.18x faster                                                   |
| bench_thread_pool       | 546 us                                                 | 464 us: 1.18x faster                                                   |
| dask                    | 265 ms                                                 | 226 ms: 1.17x faster                                                   |
| mypy2                   | 307 ms                                                 | 263 ms: 1.17x faster                                                   |
| sympy_integrate         | 13.3 ms                                                | 11.5 ms: 1.16x faster                                                  |
| async_generators        | 234 ms                                                 | 202 ms: 1.16x faster                                                   |
| unpack_sequence         | 37.4 ns                                                | 32.7 ns: 1.14x faster                                                  |
| sympy_expand            | 275 ms                                                 | 241 ms: 1.14x faster                                                   |
| sqlglot_normalize       | 196 ms                                                 | 172 ms: 1.14x faster                                                   |
| xml_etree_generate      | 54.2 ms                                                | 48.2 ms: 1.12x faster                                                  |
| regex_v8                | 17.6 ms                                                | 15.7 ms: 1.12x faster                                                  |
| sympy_str               | 169 ms                                                 | 151 ms: 1.12x faster                                                   |
| json                    | 3.08 ms                                                | 2.78 ms: 1.11x faster                                                  |
| nqueens                 | 68.2 ms                                                | 61.7 ms: 1.11x faster                                                  |
| sqlite_synth            | 1.47 us                                                | 1.34 us: 1.10x faster                                                  |
| xml_etree_parse         | 106 ms                                                 | 96.9 ms: 1.10x faster                                                  |
| mdp                     | 1.66 sec                                               | 1.51 sec: 1.10x faster                                                 |
| regex_dna               | 162 ms                                                 | 149 ms: 1.08x faster                                                   |
| sympy_sum               | 93.6 ms                                                | 86.6 ms: 1.08x faster                                                  |
| coroutines              | 20.2 ms                                                | 18.7 ms: 1.08x faster                                                  |
| pathlib                 | 28.8 ms                                                | 27.5 ms: 1.05x faster                                                  |
| json_loads              | 16.9 us                                                | 16.2 us: 1.05x faster                                                  |
| telco                   | 3.63 ms                                                | 3.51 ms: 1.04x faster                                                  |
| meteor_contest          | 78.1 ms                                                | 75.6 ms: 1.03x faster                                                  |
| xml_etree_iterparse     | 72.3 ms                                                | 70.1 ms: 1.03x faster                                                  |
| unpickle                | 9.89 us                                                | 9.74 us: 1.01x faster                                                  |
| pidigits                | 282 ms                                                 | 281 ms: 1.01x faster                                                   |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.00x slower                                                  |
| gc_traversal            | 2.39 ms                                                | 2.42 ms: 1.01x slower                                                  |
| comprehensions          | 17.6 us                                                | 17.8 us: 1.01x slower                                                  |
| unpickle_list           | 2.69 us                                                | 2.73 us: 1.01x slower                                                  |
| pickle_list             | 2.80 us                                                | 2.85 us: 1.02x slower                                                  |
| pickle                  | 7.35 us                                                | 7.50 us: 1.02x slower                                                  |
| generators              | 32.7 ms                                                | 33.9 ms: 1.04x slower                                                  |
| python_startup          | 11.9 ms                                                | 12.4 ms: 1.04x slower                                                  |
| regex_effbot            | 2.46 ms                                                | 2.62 ms: 1.06x slower                                                  |
| bench_mp_pool           | 39.7 ms                                                | 44.3 ms: 1.12x slower                                                  |
| python_startup_no_site  | 8.88 ms                                                | 10.4 ms: 1.17x slower                                                  |
| coverage                | 42.0 ms                                                | 55.4 ms: 1.32x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.21x faster                                                           |
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
